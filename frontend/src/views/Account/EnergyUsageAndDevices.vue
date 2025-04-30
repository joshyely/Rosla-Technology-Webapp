<script setup>
import ButtonPrimary from '@/components/buttons/ButtonPrimary.vue';
</script>

<template>
<div class="content" id="energy-tracking">
    <h2>View Your Energy Usage</h2>
    <div>
        <RouterLink to="/energy-tracking/dashboard">
            <ButtonPrimary>Go to Dashboard</ButtonPrimary>
        </RouterLink>
    </div>
</div>
<div class="content">
    <h2>Your Devices</h2>
    <br>
    <p style="color: var(--color-text-3); font-size: 1.1rem"><em>Sorry, this feature has not been implemented yet.</em></p>
</div>
</template>

<style scoped lang="scss">
.content{
    padding: 3% 0;
}
#energy-tracking{
    border-bottom: var(--border);
    & > div {
        padding: 2% 0;
    }
}
</style>