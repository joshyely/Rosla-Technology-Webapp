<script setup>
const props = defineProps({
    routes: {
        type: Array,
        default(rawProps){
            return [
                {
                    to: '',
                    display: 'Item'
                }
            ]
        }
    }
})
</script>

<template>
<div class="sidebar">
    <slot name="top"></slot>
    <nav>
        <RouterLink v-for="route in routes" :to="route.to">{{ route.display }}</RouterLink>
    </nav>
    <slot name="bottom"></slot>
</div>
</template>

<style scoped lang="scss">
.sidebar{
    flex: 1;
    border-bottom: var(--border);
    padding-top: 1em;
    @media(min-width: 1024px){
        border-right: 1px solid #ddd;
        border-bottom:none;
    }
    nav{
        display: flex;
        flex-direction: column;
        align-items: center;
        a{
            text-decoration: none;
            color: #333;
            padding: 10px 20px;
            width: 100%;
            text-align: left;
            display: flex;
            align-items: center;

            i {
                margin-right: 10px;
            }
            &:hover,
            &.active {
                background-color: #007bff;
                color: white;
            }
        }
    }
    img{
        width: 100px;
        height: 100px;
        border-radius: 50%;
        margin-bottom: 20px;
    }

    
}
</style>