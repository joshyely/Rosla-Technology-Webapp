<script setup>
</script>


<template>
<button 
    v-bind="$attrs"
    style="font-size: 1.2rem;"
>
    <slot>Button</slot>
</button>
</template>

<style scoped lang="scss">
button {
    border:none;
    padding: .8em 1.5em;
    border-radius: 20px;
    transition: all .25s ease-in;
    &:hover{
        filter: brightness(85%);
        cursor: pointer;
    }
    &:active{
        filter: brightness(50%);
        transform: scale(98%);
    }
    &:disabled{
        opacity: 0.8;
        cursor: not-allowed;
    }
    a.router-link-active{
        filter: brightness(50%);
    }
}
</style>