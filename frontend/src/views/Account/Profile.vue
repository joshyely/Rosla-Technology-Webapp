<script setup>
import { reactive } from 'vue';
import Form from '@/components/form/Form.vue';
import Fieldset from '@/components/form/Fieldset.vue';
import Alpha from '@/components/form/fields/Alpha.vue';
import Date from '@/components/form/fields/Date.vue';
import Submit from '@/components/form/Submit.vue';

const models = reactive({
    firstName: 'John',
    lastName: 'Doe',
    dob: ''
});
</script>

<template>
<h1>Profile</h1>
<div class="container">
    <Form>
        <template #default>
            <Fieldset heading="Full Name" heading-size="1.5rem">
                <div class="flex">
                    <Alpha
                    placeholder="First Name"
                    v-model="models.firstName"
                    ></Alpha>
                    <Alpha
                        placeholder="First Name"
                        v-model="models.lastName"
                    ></Alpha>
                </div>
            </Fieldset>
            <br>
            <Fieldset heading="Date of Birth" heading-size="1.5rem">
                <Date v-model="models.dob"></Date>
            </Fieldset>
        </template>
        <template #submit-btn>
            <div class="flex submit-container">
                <Submit value="Update Profile"></Submit>
            </div>
        </template>
    </Form>
</div>
</template>