<script setup>
import Card from '@/components/Card.vue';
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
        <img src="../assets/pageImages/home.jpg" />
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
            <article>
                <h2>Our Digital Solution</h2>
                <div class="card-container">
                    <Card style="background-color: var(--color-primary-6);"></Card>
                    <Card style="background-color: var(--color-primary-4);"></Card>
                    <Card style="background-color: var(--color-primary-6);"></Card>
                </div>
            </article>
        </section>
    </template>
</PagePrimary>
</template>

<style scoped lang="scss">
</style>