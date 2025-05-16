import { createRouter, createWebHistory } from 'vue-router'
import { loggedIn } from './utils/auth'


import Home from './views/Home.vue'
import About from './views/About.vue'
import Contact from './views/Contact.vue'
import Login from './views/Login.vue'
import Register from './views/Register.vue'
import Products from './views/Products/Products.vue'
import ProductInfo from './views/Products/ProductInfo.vue'
import Account from './views/Account/Account.vue'
import Profile from './views/Account/Profile.vue'
import Security from './views/Account/Security.vue'
import Appointments from './views/Account/Appointments.vue'
import AppointmentAbout from './views/Appointments/AppointmentAbout.vue'
import AppointmentBook from './views/Appointments/AppointmentBook.vue'
import BaseEnergyTracking from './views/EnergyTracking/Feature/BaseEnergyTracking.vue'
import TrackingDashboard from './views/EnergyTracking/Feature/TrackingDashboard.vue'
import MeterReadings from './views/EnergyTracking/Feature/MeterReadings.vue'
import EnergyTrackingAbout from './views/EnergyTracking/EnergyTrackingAbout.vue'
import EnergyUsageAndDevices from './views/Account/EnergyUsageAndDevices.vue'


const devMode = true;
const checks = {
    isLoggedIn: (to, from) => {
        if (!loggedIn.value && !devMode){
            return { name: 'Login' }
        }
    },
}

const routes = [
    { path: '/', component: Home, name: 'Home' },
    { path: '/about', component: About, name: 'About' },
    { path: '/contact', component: Contact, name: 'Contact' },
    { path: '/login', component: Login, name: 'Login' },
    { path: '/register', component: Register, name: 'Register' },
    { 
        path: '/account',
        component: Account,
        name: 'Account Dashboard',
        beforeEnter: checks.isLoggedIn,
        children: [
            {
                path: 'profile',
                component: Profile,
                name: 'Profile'
            },
            {
                path: 'security',
                component: Security,
                name: 'Account Security'
            },
            {
                path: 'appointments',
                component: Appointments,
                name: 'User Appointments'
            },
            {
                path: 'energy-and-devices',
                component: EnergyUsageAndDevices,
                name: 'User Energy Usage and Devices'
            },
        ]
    },
    { 
        path: '/products',
        component: Products, 
        name: 'Products' 
    },
    {
        path: '/products/:id',
        component: ProductInfo,
        name: 'Product Info'
    },
    {
        path: '/appointments',
        component: AppointmentAbout,
        name: 'Appointments About'
    },
    {
        path: '/appointments/book',
        component: AppointmentBook,
        name: 'Appointments Book',
        beforeEnter: checks.isLoggedIn,
    },
    {
        path: '/energy-tracking',
        component: BaseEnergyTracking,
        name: 'Energy Tracking',
        beforeEnter: checks.isLoggedIn,
        children: [
            {
                path: 'dashboard',
                component: TrackingDashboard,
                name: 'Energy Tracking Dashboard'
            },
            {
                path: 'meter-readings',
                component: MeterReadings,
                name: 'Energy Tracking Meter Readings'
            },
        ]
    },
    {
        path: '/about/energy-tracking',
        component: EnergyTrackingAbout,
        name: 'About Energy Tracking',
    },
]

const router = createRouter({
    history: createWebHistory('/Rosla-Technology-Webapp/'),
    routes,
});

export default router;