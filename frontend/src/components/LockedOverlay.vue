<script setup>
import Padlock from './icons/Padlock.vue';

const props = defineProps({
    heading: String,
    headingSize: {
        type: String,
        default: '1.6rem'
    },
    headingWeight: {
        type: String,
        default: '500'
    },
})
</script>

<template>
<div class="locked-overlay">
    <div class="content-container">
        <slot></slot>
    </div>
    <div class="overlay">
        <div class="overlay-icon">
            <Padlock></Padlock>
        </div>
        <span 
            class="overlay-heading"
            :style="{
                fontSize: headingSize,
                fontWeight: headingWeight,
            }"
        >
            {{ heading }}
        </span>
    </div>
</div>
</template>

<style scoped lang="scss">
.locked-overlay{
    position: relative;
    padding: 1%;
    
    .content-container{
        filter: blur(10px);
    }
    .overlay{
        $color: rgb(230, 230, 230);
        top: 0;
        padding: 15% 3%;
        width:100%;
        min-height:100%;
        max-height: fit-content;
        position: absolute;
        background: rgb(50, 50, 50, .6);
        display:flex;
        flex-direction: column;
        align-items: center;
        border-radius: var(--border-radius);
        color: $color;
        fill: $color;
        .overlay-icon{
            display:flex;
            justify-content: center;
            svg{
                --size: 20%;
            }
        }
        .overlay-heading{
            display:block;
        }
    }
}
</style>