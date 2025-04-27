<script setup>
const props = defineProps({
    heading: String,
    headingWeight: String,
    headingSize: String,
});
</script>

<template>
<fieldset>
    <h2 
        v-if="!!heading" 
        class="fieldset-heading"
        :style="{
            fontWeight: headingWeight,
            fontSize: headingSize,
        }"
    >
        {{ props.heading }}
    </h2>
    <div class="fieldset-content" v-bind="$attrs">
        <slot></slot>
    </div>
</fieldset>
</template>

<style scoped lang="scss">
fieldset{
    .fieldset-content {
        display:flex;
        flex-direction: column;
        align-items: center;
        & > *{
            width: 95%;
        }
    }
    border: none;
    .fieldset-heading {
        padding: .8vh 5%;
        margin-bottom: 1.5vh;
        border-bottom: var(--border);
        font-size: 1.6rem;
        font-weight: 400;
    }
}
</style>