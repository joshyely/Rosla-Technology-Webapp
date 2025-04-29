<script setup>
import PagePrimary from '@/templates/PagePrimary.vue';
import ButtonPrimary from '@/components/buttons/ButtonPrimary.vue';
import ButtonSecondary from '@/components/buttons/ButtonSecondary.vue';
import placeholders from '@/utils/placeholders';
</script>

<template>
<PagePrimary>
<template #top-container>
    <div>
        <h1>Book an appointment with us</h1>
    </div>
    <div>
        <RouterLink to="/appointments/book">
            <ButtonPrimary>Book Now</ButtonPrimary>
        </RouterLink>
    </div>
</template>
<template #top-image-container>
    <img src="@/assets/images/pages/appointment-about.jpg" />
</template>
<template #section>
    <section class="full" id="about-appointments">
        <div class="flex">
            <div class="text-container">
                <article>
                    <h3>
                        Installations
                    </h3>
                    <div class="img-container">
                        <img src="@/assets/images/installations.jpg" alt="Engineer installing solar panel on house">
                    </div>
                    <p>
                        <strong>Ready to upgrade your home with clean, smart energy?</strong> Booking an installation with Rosla is fast and easy!
                    </p>
                    <p>
                        Once you have chosen your solar or smart device package, simply schedule your installation appointment online or by phone. 
                        Our certified technicians will arrive fully prepared to install your system efficiently and professionally.
                        
                    </p>
                    <p>
                        We work around your schedule, with flexible dates and times, to ensure the process is seamless and minimally disruptive.
                    </p>
                </article>
            </div>
            <div class="text-container">
                <article>
                    <h3>
                        Consultations
                    </h3>
                    <div class="img-container">
                        <img 
                            src="@/assets/images/consultations.jpg" 
                            alt="Professional discussion between a customer and and an employee"
                        >
                    </div>
                    <p>
                        <strong>Not sure what solution fits your home best?</strong> Book a free consultation with Rosla's green energy experts.
                    </p>
                    <p>
                        During your consultation, we'll assess your property, discuss your energy goals, 
                        and recommend tailored solutions that maximize efficiency and savings.
                    </p>
                    <p>
                        Consultations can be done virtually or in-person, and appointments are available at times that suit your lifestyle.
                    </p>
                    <p>
                        Get clear answers and a custom plan <em>— no pressure, just real advice.</em>
                    </p>
                </article>
            </div>
            <div class="text-container">
                <article>
                    <h3>
                        Manage and view your appointments
                    </h3>
                    <div class="img-container">
                        <img src="@/assets/images/manage-appointments.jpg" alt="Person viewing their appointments from their phone">
                    </div>
                    <p>
                        <strong>Need to cancel or reschedule an appointment with us?</strong> No worries! We know that life can get in the way sometimes.
                    </p>
                    <p>
                        You can view all upcoming appointments under your account and choose to either reschedule or cancel.
                    </p>
                </article>
                <div class="cta-container">
                    <RouterLink to="account/appointments">
                        <ButtonPrimary>View your appointments here</ButtonPrimary>
                    </RouterLink>
                </div>
            </div>
        </div>
    </section>
    <div class="section-wrapper" style="background: var(--color-primary-4)">
        <section class="full" id="booking-faq">
            <div class="flex">
                <div class="container container-left">
                    <img src="@/assets/blankImage.png" alt="Blank Image" width="80%" style="object-fit: contain;">
                </div>
                <div class="container container-right" id="booking-cta-container">
                    <h2>
                        Ready to book an appointment with us?
                    </h2>
                    <div>
                        <RouterLink to="">
                            <ButtonPrimary
                                button-color="var(--color-primary-1)"
                                style="
                                    font-size: 1.6rem;
                                    width: 100%;
                                    height: 13vh;
                                "
                            >
                                Book Now!
                            </ButtonPrimary>
                        </RouterLink>
                    </div>
                </div>
            </div>
        </section>
    </div>
    
</template>
</PagePrimary>
</template>

<style scoped lang="scss">
.text-container{
    h3{
        line-height: normal;
        margin-bottom: 2vh;
    }
    p{
        margin-bottom: .8vh;
    }
    .cta-container{
        padding: 10% 0;
    }
}


#about-appointments{
    padding-bottom: 13vh;
    .flex{
        gap: max(8%, 5vh);
        .text-container{
            flex:1;
            .img-container{
                margin:auto;
                width: min(100%, 500px);
            }
        }
    }
}
#booking-faq{
    .flex{
        .container-left{
            flex: 5;
        }
        .container-right{
            flex: 2;
            & > div{
                padding: 5vh 0;
            }
        }
    }
}
</style>