<script setup>
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
    padding: 0 5%;
    text-align: center;
    h1{
        margin-bottom: 2.5rem;
    }
    @media(min-width: 1024px){
        text-align: start;
        padding: 0;
    }
}
</style>