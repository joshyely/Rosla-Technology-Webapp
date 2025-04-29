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
    <div class="account-section">
        <Form
            submit-value="Update"
        >
            <Fieldset heading="Full Name">
                <div class="flex">
                    <Alpha
                        v-model="models.firstName"
                        placeholder="First Name"
                    ></Alpha>
                    <Alpha
                        v-model="models.lastName"
                        placeholder="Last Name"
                    ></Alpha>
                </div>
            </Fieldset>
            <Fieldset heading="Date of Birth">
                <Date></Date>
            </Fieldset>
        </Form>
    </div>
</div>
</template>

<style lang="scss">
.account-section{
    width: 80%;
    fieldset{
        .fieldset-heading{
            font-size: 1.2rem;
        }
    }
}
</style>