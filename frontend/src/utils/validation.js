export const validPattern = (value, pattern) => pattern==null || pattern.test(value);

export const notEmpty = (value) => {
    if (value == null) {
        return true
    }
    return value.trim() != ''
};

export const sameAs = (value, compare) => {
    if(!value || !compare){
        return null
    }

    switch(compare.constructor){
        case String || Number || Boolean:
            return value == compare
        case Array:
            for(i of compare){
                if (value != compare) {
                    return false
                }
            }
            return true
        default:
            return null
    }
};

export const differentTo = (value, compare) => {
    if(
        compare == null
    ){
        return null
    }

    switch(compare.constructor){
        case String || Number || Boolean:
            return value != compare
        case Array:
            for(i of compare){
                if (value == compare) {
                    return false
                }
            }
            return true
        default:
            return null
    }
};



export const validateMatch = (value, compare, errMsgRef, displayMsg='Fields do not match.') => {
    let result = sameAs(value, compare);
    if(result == null){
        return true
    }
    else if (result == false){
        errMsgRef.msg = displayMsg;
        return false
    }
    errMsgRef.msg = '';
    return true;
}