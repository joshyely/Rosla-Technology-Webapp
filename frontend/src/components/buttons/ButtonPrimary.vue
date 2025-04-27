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
    class="button-primary"
    :style="{
        background: buttonColor,
        color: textColor
    }"
>
<slot>Primary</slot>
</Button>
</template>