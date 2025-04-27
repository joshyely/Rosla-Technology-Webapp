<script setup>
import Card from '@/components/Card.vue';

</script>

<template>
<div class="page-top">
    <div class="top-overlay-container">
        <div class="top-container">
            <slot name="top-container"></slot>
        </div>
    </div>
    <div class="top-image-container">
        <slot name="top-image-container"></slot>
    </div>
</div>
<slot name="section">

</slot>
</template>

<style lang="scss">
.top-container{
    h1{
        margin-bottom: 2.5rem;
    }
}
</style>