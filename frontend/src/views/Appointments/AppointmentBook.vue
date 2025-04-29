<script setup>
import { reactive } from 'vue';
import Form from '@/components/form/Form.vue';
import Fieldset from '@/components/form/Fieldset.vue';
import TextArea from '@/components/form/fields/TextArea.vue';
import Select from '@/components/form/Select.vue';
import Input from '@/components/form/Input.vue';


const options = {
    appointmentType: {
        'installation': 'Installation',
        'consultation': 'Consultation'
    },
    userAddresses: {
        '21 Apple Street, London':'21 Apple Street, London'
    },
    availableDates: {
        'May 2, 2025': 'Friday, May 2, 2025',
        'May 3, 2025': 'Saturday, May 3, 2025',
        'May 5, 2025': 'Monday, May 5, 2025',
        'May 6, 2025': 'Tuesday, May 6, 2025',
        'May 7, 2025': 'Wednesday, May 7, 2025',
    },
    availableTimeSlots: {
        'May 2, 2025': {
            '9:00-10:30': '9:00-10:30',
            '10:30-12:00': '10:30-12:00',
            '15:00-16:30': '15:00-16:30',
            '16:30-18:00': '16:30-18:00'
        },
        'May 3, 2025': {
            '9:00-10:30': '9:00-10:30',
            '10:30-12:00': '10:30-12:00',
        },
        'May 5, 2025': {
            '10:30-12:00': '10:30-12:00',
            '15:00-16:30': '15:00-16:30',
            '16:30-18:00': '16:30-18:00'
        },
        'May 6, 2025': {
            '9:00-10:30': '9:00-10:30',
            '10:30-12:00': '10:30-12:00',
            '12:00-13:30': '12:00-13:30',
            '13:30-15:00': '13:30-15:00',
            '15:00-16:30': '15:00-16:30',
            '16:30-18:00': '16:30-18:00'
        },
        'May 7, 2025': {
            '9:00-10:30': '9:00-10:30',
            '10:30-12:00': '10:30-12:00',
            '12:00-13:30': '12:00-13:30',
            '13:30-15:00': '13:30-15:00',
            '15:00-16:30': '15:00-16:30',
            '16:30-18:00': '16:30-18:00'
        },
    },
    topics: {
        'smart meter installation': 'Smart meter installation',
        'solar panel installation': 'Solar panel installation',
        'other': 'Other',
    },
    devices: {
        1: 'Rosla Smart Meter',
        2: 'Rosla Solar Panel',
    }
}




const models = reactive({
    appointmentType: '',
    notes: '',
    date: '',
    timeslot: '',
    device: '',
    topic: ''
})

</script>


<template>

<section class="form">
    <h1>Book Appointment</h1>
    <br>
    <div class="container info-container" id="user-info">
        <p>Full name: <span>John Doe</span></p>
        <p>Email: <span>johndoe@example.com</span></p>
        <p>Phone: <span>0123456789</span></p>
    </div>
    <Form id="appointment-book-form">
        <Fieldset>
            <Select
                required
                placeholder="Appointment Type"
                v-model="models.appointmentType"
                :options="options.appointmentType"
            ></Select>
           
        </Fieldset>
        <Fieldset v-show="!!models.appointmentType">
            <Select 
                v-if="models.appointmentType === 'installation'"
                v-model="models.device"
                :options="options.devices"
                placeholder="Device to install"
           ></Select>
           <Select
                v-else-if="models.appointmentType === 'consultation'"
                v-model="models.topic"
                :options="options.topics"
                placeholder="Consultation topic"
            ></Select>
            
            <TextArea
                v-if="models.topic === 'other'"
                rows="5"
                placeholder="Brielfy describe what the consultation will be about"
            ></TextArea>
        </Fieldset>
        <Fieldset>
            <Select
                required
                placeholder="Address"
                :options="options.userAddresses"
            ></Select>
        </Fieldset>
        <Fieldset
            heading=""
        >
            <div class="flex" id="datetime-select">
                <div id="date-select">
                    <Select
                        :options="options.availableDates"
                        v-model="models.date"
                        placeholder="Date"
                    ></Select>
                </div>
                <div id="timeslot-select">
                    <Select
                        :options="options.availableTimeSlots[models.date]"
                        v-model="models.timeslot"
                        placeholder="Timeslot"
                    ></Select>
                </div>
            </div>
        </Fieldset>
    </Form>
</section>
</template>

<style scoped lang="scss">
#datetime-select{
    height: 100%;
    & > div{
        .select-wrapper{
            width:100%;
        }
    }
    #date-select{
        flex:2;
    }
    #timeslot-select{
        flex:1;
    }
}
#user-info{
    padding: 5% 5% 2%;
    border-bottom: var(--border);
    @media(min-width: 1024px){
        display: grid;
        grid-template-columns: 1fr 1fr;
    } 
}
</style>