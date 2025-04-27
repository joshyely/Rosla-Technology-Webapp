<script setup>
import { formatPrice } from '@/utils/currency';
import Products from '@/views/Products/Products.vue';

const props = defineProps({
    product: {
        type: Object,
        default(rawProps) {
            return { 
                id: 1,
                name: 'Product',
                description: 'No Description',
                imageUrl: 'src/assets/blankImage.png',
                price: 1,
                discount: {
                    amount: 0,
                    percent: 0
                }
            }
        }
    }
})
</script>

<template>
<div class="product-card">
    <a :href="'products/' + product.id">
        <img :src="Products.imageUrl" alt="image">
        <div class="product-about">
            <h2 class="product-name">{{ product.name }}</h2>
            <span class="product-description">{{ product.description }}</span>
        </div>
        <div class="product-price-info">
            <span class="product-price">{{formatPrice(product.price)}}</span>
        </div>
    </a>        
</div>
</template>

<style lang="scss">
.product-card{
    border-radius: var(--border-radius-2);
    overflow: hidden;
    box-shadow: var(--box-shadow);
    transition: all .1s ease-in-out;
    max-height: 30em;
    flex: 1;
    & > *{
    width:100%;
    }
    &:hover{
        box-shadow: var(--box-shadow-hover);
        transform: scale(.99);
    }
    a{
        height:100%;
        text-decoration: none;
        color:var(--color-text);
        display: flex;
        flex-direction: column;
        img{
            object-fit: contain;
            width:100%;
            flex: 2;
        }
        .product-about{
            flex: 1;
            padding: 2% 5%;
            .product-name{
                font-size: 1.5rem;
            }
        }
        .product-price-info{
            display:flex;
            flex:1;
            justify-content: center;
            align-items: end;
            padding: 1em 1.5em;
            .product-price{
                font-size: 1.2rem;
                font-weight:600;
            }
        }
    }
    
}
</style>