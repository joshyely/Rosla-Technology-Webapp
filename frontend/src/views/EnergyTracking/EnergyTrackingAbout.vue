<script setup>
import PagePrimary from '@/templates/PagePrimary.vue';
import ButtonPrimary from '@/components/buttons/ButtonPrimary.vue';
</script>

<template>
<PagePrimary>
    <template #top-container>
        <div>
            <h1>Track your energy usage</h1>
        </div>
        <div>
            <RouterLink to="/energy-tracking/dashboard">
                <ButtonPrimary
                    button-color="var(--color-secondary-3)"
                >Go to Dashboard</ButtonPrimary>
            </RouterLink>
        </div>
    </template>
    <template #top-image-container>
        <img src="@/assets/images/pages/energy-tracking-about.jpg" />
    </template>
    <template #section>
        <section class="full bottom-padding">
            <div class="flex article-row">
                <div class="text-container">
                    <article>
                        <h3>View Your Energy Usage</h3>
                        <div class="img-container">
                            <img src="@/assets/images/graph-graphic.jpg" alt="graphic of column graph">
                        </div>
                        <p>
                            <strong>Rosla gives you full visibility into your energy habits.</strong>
                            You can easily view both <strong>past</strong> and <strong>current</strong> energy usage through your <strong>personal dashboard</strong>. 
                        </p>
                        <p>
                            Whether you're checking daily trends or monthly totals, the data is clear, up-to-date, 
                            and easy to understand — <em>helping you stay in control and make smarter energy decisions.</em>
                        </p>
                    </article>
                </div>
                <div class="text-container">
                    <article>
                        <h3>Submit Meter Readings</h3>
                        <div class="img-container">
                            <img src="@/assets/images/meter-graphic.jpg" alt="graphic of meter reading">
                        </div>
                        <p>
                            <strong>Submitting your meter readings with Rosla takes seconds.</strong> Just log in, enter your reading, 
                            and you're done. 
                        </p>
                        <p>
                            No waiting on hold or mailing forms — <em>it's simple, accurate, and ensures 
                            your billing reflects your actual usage.</em>
                        </p>
                    </article>
                </div>
                <div class="text-container">
                    <article>
                        <h3>Track how much you are being billed</h3>
                        <div class="img-container">
                            <img src="@/assets/images/cash-graphic.jpg" alt="graphic of stack of cash">
                        </div>
                        <p>
                            <strong>Stay on top of your energy costs</strong> with real-time billing tracking. Rosla shows you exactly 
                            how much you're being charged, with breakdowns by usage, time period, and device. 
                        </p>
                        <p>
                            No surprises — <em>just clear, transparent billing you can trust.</em>
                        </p>
                    </article>
                </div>
            </div>
        </section>
    </template>
</PagePrimary>
</template>

<style scoped lang="scss">
.img-container{
    padding: 5% 13%;
}
</style>