<script setup>
import Arrow from '@/components/buttons/GridAccordion.vue';
import AccordionChevron from './icons/AccordionChevron.vue';
import { ref } from 'vue';
const props = defineProps({
    heading: {
        type: String,
        default: 'Heading'
    },
    headingSize: {
        type: String,
        default: '1.3rem'
    },
    headingWeight: {
        type: String,
        default: '500'
    },
    headerBackground: {
        stype: String,
        default: ''
    }
})

const show = ref(false);

const toggleShow = () => show.value = !show.value;
</script>

<template>
<div class="accordion">
    <div class="accordion-header" @click="toggleShow" :style="{fontSize: headingSize}">
        <div class="icon">
            <AccordionChevron :class="!show ? '' : 'active'"></AccordionChevron>
        </div>
        <div class="heading">
            <slot name="heading">
                <h2 class="heading-text" :style="{fontWeight: headingWeight}">{{ heading }}</h2>
            </slot>
        </div>
    </div>
    <div id="content" class="accordion-content" v-show="show">
        <slot></slot>
    </div>
</div>
</template>
<style lang="scss">
.accordion {
    border-bottom: var(--border);
    .accordion-header{
        --transition: all .5s ease-in-out;
        --color: var(--color-primary-2);
        display:flex;
        align-items: center;
        transition: var(--transition);
        padding: 1% 0;
        .icon{
            width: fit-content;
        }
        .heading{
            flex: 1;
            padding: 0 1%;
            .heading-text{
                font-size: 1.3em;
            }
        }
        &:hover{
            color: var(--color);
            .icon{
                svg{
                    transition: var(--transition);
                    fill: var(--color);
                }
            }
        }
    }
    .accordion-content{
        padding: 1% 1% 2%;
    }   
}
</style>