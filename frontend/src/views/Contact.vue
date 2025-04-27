<script setup>
import Card from '@/components/Card.vue';
import PagePrimary from '@/templates/PagePrimary.vue';
import { ref, reactive } from 'vue';
import Form from '@/components/form/Form.vue';
import Fieldset from '@/components/form/Fieldset.vue';
import Alpha from '@/components/form/fields/Alpha.vue';
import Email from '@/components/form/fields/Email.vue';
import TextArea from '@/components/form/fields/TextArea.vue';
import { apiJSON } from '../utils/axiosAPI';

const models = reactive({
    fName: '',
    lName: '',
    email: '',
    message: '',
});

const contact = {
    email: 'name@example.com',
    phone: '0123456789',
    address: '42 East Street London',
    postcode: 'AB2 CD4 '
}

</script>


<template>
<PagePrimary>
    <template #top-container>
        <h1>Contact Us</h1>
    </template>
    <template #top-image-container>
        <img src="../assets/pageImages/home.jpg" />
    </template>
    <template #section>
        <section class="full">
            <div class="flex">
                <div class="container flex-secondary" id="contact-info">
                    <article>
                        <h2>How you can reach us:</h2>
                        <p>
                            Feel free to reach out to us through the <strong>contact form</strong>. 
                        </p>
                        <p>
                            You can also contact us through <strong>phone</strong> or <strong>email</strong>.
                        </p>
                        <br>
                        <p><i>📞</i> {{ contact.phone }}</p>
                        <p><i>✉️</i> {{ contact.email }}</p>
                        <p><i>📍</i>{{ contact.address }}, {{ contact.postcode }}</p>
                    </article>
                </div>
                <div class="container flex-primary" id="contact-form">
                    <Form>
                        <Fieldset>
                            <div class="flex">
                                <Alpha id="fName" placeholder="First Name" required v-model="models.fName"></Alpha>
                                <Alpha id="lName" placeholder="Last Name" required v-model="models.lName"></Alpha>
                            </div>
                            <Email v-model="models.email" required></Email>
                        </Fieldset>
                        <Fieldset>
                            <TextArea v-model="models.message" name="message" rows="8" placeholder="Type your message ..."></TextArea>
                        </Fieldset>
                    </Form>
                </div>
            </div>
        </section>
    </template>
</PagePrimary>
</template>

<style scoped lang="scss">
#contact-form{
    @media(min-width: 1024px){
        border-top:none;
    }
    border-top: var(--border)
}
</style>