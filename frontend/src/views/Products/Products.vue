<script setup>
import ProductCard from '@/components/ProductCard.vue';

const products = [
    {
        id: 1,
        name: 'Solar Panel',
        description: 'A cutting edge solar panel.',
        price: 139999,
        imageUrl: 'src/assets/blankImage.png',
    },
    {
        id: 2,
        name: 'Smart Plug',
        description: 'Track your electricity usage and manage your home devices.',
        price: 18954,
        imageUrl: 'src/assets/blankImage.png',
    },
    {
        id: 3,
        name: 'Smart Thermostat',
        description: 'No Description',
        price: 18099,
        imageUrl: 'src/assets/blankImage.png',
    },
    {
        id: 4,
        name: 'Smart Fridge',
        description: 'No Description',
        price: 18099,
        imageUrl: 'src/assets/blankImage.png',
    },
]
</script>

<template>
<section class="full">
    <h1>Products</h1>
    <div class="products-grid loading">
        <ProductCard v-for="product in products"
            :product="product"
        ></ProductCard>
        <ProductCard v-for="num in 8"
        ></ProductCard>
    </div>
</section>
</template>

<style lang="scss">
.products-grid{
    display:grid;
    @media(min-width: 1024px){
        grid-template-columns: 1fr 1fr 1fr 1fr;
    }
    grid-template-columns: 1fr 1fr;
    grid-auto-rows: 45vh;
    gap: 40px;
    width:100%;
}
</style>