<script setup>
import Button from './Button.vue';
const props = defineProps({
    buttonColor: {
        type: String,
        default: 'var(--color-primary-2)'
    },
    textColor: {
        type: String,
        default: 'rgb(255, 255, 255)'
    },
})
</script>

<template>
<Button
    class="button-secondary"
    :style="{
        borderColor: buttonColor,
        color: textColor
    }"
>
<slot>Secondary</slot>
</Button>
</template>
<style scoped lang="scss">
.button-secondary {
    border-style: solid;
    border-width: 2px;
}
</style>