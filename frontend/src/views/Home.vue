<script setup>
import { reactive, ref, provide } from 'vue';
import Card from '@/components/cards/CardColored.vue';
import Grid from '@/components/Grid.vue';
import Accordion from '../components/Accordion.vue';
import Article from '@/components/Article.vue';
import TextButton from '@/components/buttons/Button.vue';

const viewImage = '/src/assets/viewImages/home.png';



</script>

<template>
<div class="home-page-top flex" id="home-top">
    <div class="home-top-container container">
        <div class="page-intro">
            <h1 class="title">Helping homeowners save money and reduce their carbon footprint</h1>
            <p>We install smart electricity & gas meters and solar panels and allow you to track your usage through the convenience of your phone.</p>
        </div>
    </div>
    <div class="home-top-image-container">
        <img src="../assets/images/pages/home.jpg" />
        <div class="overlay"></div>
    </div>
</div>
<section class="full" style="background-color: var(--color-backgroud-soft);">
    <h2>Only 37% of homes in the UK consistently track their energy usage. Why should you?</h2>
    <br>
    <div class="flex" id="home-cards">
        <Card style="background-color: var(--color-primary-6);"></Card>
        <Card style="background-color: var(--color-primary-4);"></Card>
        <Card style="background-color: var(--color-primary-6);"></Card>
    </div>
</section>

</template>

<style scoped lang="scss">
.container{
    padding: 2em 3em;
}

.mobile{
    .page-top{
        grid-template-columns: 1fr;
    }
}

.home-page-top {
    height: fit-content;
    width: 100%;
    background-color: var(--color-primary-5);

    .home-top-image-container {
        flex: 3;
        display:block;
        min-height: 100%;
        overflow: hidden;
        img {
            object-fit:cover;
            width: 100%;
            height:100%;
        }
    }
    .home-top-container {
        flex: 2;
        
        color: var(--color-text);
        height:100%;
        p{
            font-size: 1.15rem;
        }
    }
}

.content {
    display: flex;
    width: 100%;
    justify-content: center;
}

#home-cards{
    gap: 5vh;
}

.main-wrapper {
    padding: 0;
}
</style>
