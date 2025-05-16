from sqlalchemy.orm import Session, Query
from typing import Type, List
from pydantic import BaseModel
from .base_models import Base
from app.core import log

logger = log.get_logger(__name__, 'DEBUG')

class BaseRepository():
    
    def __init__(self, entity_cls: Type[Base]):
        logger.debug(
            'Initialising Crud Repository for %s..',
            entity_cls.__name__
        )

        self.entity_cls = entity_cls
        self.entity_name = entity_cls.__name__

    def __query(self, db: Session, *filters, **kw_filters) -> Query[Base]:
        logger.debug(
            'Querying %s.. Filters: \n%s\n%s',
            self.entity_name,
            filters,
            kw_filters,
        )
        return db.query(self.entity_cls).filter(*filters).filter_by(**kw_filters)
    
    def __query_many(
        self, db: Session, *filters, skip: int = 0, limit: int = 100, **kw_filters
    ) -> Query[Base]:
        logger.debug(
            'Querying many for %s with pagination skip %s and limit %s.. \nFilters: \n%s\n%s',
            self.entity_name,
            skip,
            limit,
            filters,
            kw_filters,
        )
        return (
            db.query(self.entity_cls)
            .filter(*filters)
            .filter_by(**kw_filters)
            .offset(skip)
            .limit(limit)
        )

    def get_one(self, db: Session, *filters, **kw_filters) -> Base | None:
        logger.debug(
            'Retrieving record for %s..',
            self.entity_name,
        )
        return self.__query(db, *filters, **kw_filters).first()


    def get_many(
        self, db: Session, *filters, skip: int = 0, limit: int = 100, **kw_filters
    ) -> List[Base]:
        logger.debug(
            'Retrieving many records for %s with pagination skip %s and limit %s.. \nFilters: \n%s\n%s',
            self.entity_name,
            skip,
            limit,
            filters,
            kw_filters,
        )
        return self.__query_many(db, *filters, skip=skip, limit=limit, **kw_filters).all()


    def create(self, db:Session, schema: BaseModel) -> Base:
        logger.debug(
            'Creating entry for %s with schema: %s..',
            self.entity_name,
            schema.__repr__(),
        )
        entity_obj = self.entity_cls(**schema.model_dump())
        db.add(entity_obj)
        db.commit()
        db.refresh(entity_obj)
        return entity_obj
    
    def update(self, db: Session, entity_obj: Base) -> Base:
        logger.debug(
            'Updating entry for %s..',
            self.entity_name,
        )
        db.commit()
        db.refresh(entity_obj)
        return entity_obj

    def update_with_schema(self, db: Session, entity_obj: Base, schema: BaseModel) -> Base:
        logger.debug(
            'Updating entry for %s with schema: %s..',
            self.entity_name,
            schema.__repr__(),
        )

        # Get the schema as a dictionary and exclude any fields set to None
        schema_dict = schema.model_dump(
            exclude_unset=True
        )
        # Loop through inputted fields, updating the queried user's fields
        for field, value in schema_dict.items():
            setattr(entity_obj, field, value)
        db.add(entity_obj)
        db.commit()
        db.refresh(entity_obj)
        return entity_obj
    
    def delete(self, db: Session, entity_obj: Base) -> Base:
        logger.debug(
            'Deleting entry for %s..',
            self.entity_name,
        )

        db.delete(entity_obj)
        db.commit()
        return entity_obj