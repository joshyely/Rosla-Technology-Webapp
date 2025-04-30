<script setup>
import { ref, reactive } from 'vue';
import PageSidebar from '@/templates/PageSidebar.vue';
import Sidebar from '@/components/Sidebar.vue';

const routes = [
    {
        to: '/energy-tracking/dashboard',
        display: 'Dashboard'
    },
    {
        to: '/energy-tracking/meter-readings',
        display: 'Meter Readings'
    },
]

</script>

<template>
<PageSidebar id="energy-tracking-sidebar">
    <Sidebar
        heading="Energy Tracking"
        :routes="routes"
    >
    </Sidebar>
</PageSidebar>
</template>

<style lang="scss">
#energy-tracking-sidebar{
    .sidebar-btn{
        &.router-link-active,
        &:hover{
            background: var(--color-secondary-3) !important;
        }
    }
}

</style>
