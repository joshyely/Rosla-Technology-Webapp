<script setup>
import placeholders from '@/utils/placeholders';

const props = defineProps({
    heading: {
        type: String,
        default: placeholders.heading,
    },
    text: {
        type: String,
        default: placeholders.paragraph,
    },
    imageSrc: String,
    imageAlt: String,
});

</script>

<template>
    <div class="card">
        <div class="content">
            <slot>
                <img src="../assets/blankImage.png" alt="Blank Image">
            </slot>
            
            <p class="card-heading noto-sans-bold">{{ props.heading }}</p>
            <p>{{ props.text }}</p>
        </div>
    </div>
</template>

<style scoped lang="scss">
.card {
    box-shadow: var(--box-shadow);
    border-radius: var(--border-radius-2);
    transition: all .25s ease-in;
    padding: 10px 0;
    img {
        object-fit: cover;
        width:100%;
    }
    .content{
        padding: 15px 24px 20px;
    }
    .card-heading {
        margin: 1vh 0;
        font-size: 1.3rem;
    }
    &:hover {
        box-shadow: var(--box-shadow-hover);
    }
}
</style>