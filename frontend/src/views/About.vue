<script setup>
import Card from '@/components/cards/CardColored.vue';
import PagePrimary from '@/templates/PagePrimary.vue';
</script>


<template>
<PagePrimary>
    <template #top-container>
        <h1>About Rolsa Technologies</h1>
        <p>We are committed to shaping a sustainable future by providing innovative green energy solutions. </p>
        <p>We install smart electricity & gas meters and solar panels and allow you to track your usage through the convenience of your phone.</p>
    </template>
    <template #top-image-container>
        <img src="@/assets/images/pages/about.jpg" />
    </template>
    <template #section>
        <section class="mid">
            <article>
            <h2>Our Mission</h2>
            <p>
                We believe in making renewable energy accessible and practical for everyone. 
                Our goal is to help individuals and businesses reduce their carbon footprint 
                while maximizing energy efficiency.
            </p>
            </article>
            <br>
            <article>
                <h2>Our Digital Solution</h2>
                
            </article>
        </section>
    </template>
</PagePrimary>
</template>

<style scoped lang="scss">
</style>