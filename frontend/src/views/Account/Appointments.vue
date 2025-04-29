<script setup>
import ButtonPrimary from '@/components/buttons/ButtonPrimary.vue';
import AppointmentCard from '@/components/cards/AppointmentCard.vue';

const appointments = {
    upcoming: [
        {
            title: 'Appointment Title',
            type: 'Appointment Type',
            status: 'scheduled',
            datetime: 'May 2, 2025 · 10:00 AM',
            location: '123 Greenway Blvd',
            employee: {
                fullName: 'Sarah Johnson',
                title: 'Senior Engineer'
            },
        },
    ],
    past: [
        {
            title: 'Appointment Title',
            type: 'Appointment Type',
            status: 'completed',
            datetime: 'May 2, 2025 · 10:00 AM',
            location: '123 Greenway Blvd',
            employee: {
                fullName: 'Sarah Johnson',
                title: 'Senior Engineer'
            },
        },
        {
            title: 'Appointment Title',
            type: 'Appointment Type',
            status: 'completed',
            datetime: 'January 22, 2025 · 11:40 AM',
            location: '123 Greenway Blvd',
            employee: {
                fullName: 'Sarah Johnson',
                title: 'Senior Engineer'
            },
        },
        {
            title: 'Appointment Title',
            type: 'Appointment Type',
            status: 'completed',
            datetime: 'October 4, 2024 · 14:35 AM',
            location: '123 Greenway Blvd',
            employee: {
                fullName: 'Sarah Johnson',
                title: 'Senior Engineer'
            },
        },
    ]
}
</script>

<template>
<h1>Appointments</h1>
<br>
<div class="container" id="book-appointment-container">
    <RouterLink to="">
        <ButtonPrimary button-color="var(--color-primary-1)">Book Appointment</ButtonPrimary>
    </RouterLink>
</div>
<div class="container" id="appointments-list-container">
    <div>
        <h2>Upcoming</h2>
        <br>
        <div class="appointments-list">
            <AppointmentCard v-for="appointment in appointments.upcoming" :appointment="appointment"></AppointmentCard>
        </div>
    </div>
    <div>
        <h2>Past</h2>
        <br>
        <div class="appointments-list">
            <AppointmentCard v-for="appointment in appointments.past" :appointment="appointment"></AppointmentCard>
        </div>
    </div>
</div>
</template>

<style scoped lang="scss">
#book-appointment-container{
    border-bottom: var(--border);
    padding: 3% 2%;
}
#appointments-list-container{
    & > div {
        padding-bottom: 10vh;
        h2{
            font-weight: 400;
        }
    }
    
    .appointments-list{
        padding: 0 3%;
        display:flex;
        flex-direction: column;
        gap: 30px;
    }
}
</style>