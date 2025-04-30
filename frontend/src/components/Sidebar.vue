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
    },
    heading: String,
})
</script>

<template>
<div class="sidebar">
    <slot name="top">
        <span class="sidebar-heading" v-show="!!heading">{{ heading }}</span>
    </slot>
    <nav>
        <RouterLink 
            v-for="route in routes" 
            :to="route.to"
            class="sidebar-btn"
        >
            {{ route.display }}
        </RouterLink>
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
        .sidebar-btn{
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
            &.router-link-active {
                background-color: var(--color-primary-2);
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
    .sidebar-heading{
        display:block;
        font-size: 1.5rem;
        font-weight: 500;
        margin-bottom: 1vh;
    }
    
}
</style>