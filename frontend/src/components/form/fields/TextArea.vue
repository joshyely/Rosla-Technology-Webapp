<script setup>
import InputContainer from '../InputContainer.vue';

const regex = /^[a-zA-Z]+$/;
const errors = {
    pattern: 'Field can only contain alphabetical characters.',
}

</script>

<template>
<InputContainer>
    <textarea v-bind="$attrs" style="resize: none;"></textarea>
</InputContainer>
</template>

<style scoped lang="scss">
textarea{
    min-width: 100%;
    max-width: 100%;
    background: none;
    border: none;
    padding: .8em 1.2em 0 1.2em;
    font-size: 1rem;
    font-family: Arial, Helvetica, sans-serif;
    &:focus{
        border:none;
        outline: none;
    }
    &::-ms-clear
    {
        display: none;
    }
}
</style>