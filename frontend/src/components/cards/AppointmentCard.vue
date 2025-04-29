<script setup>
const props = defineProps({
    appointment: {
        type: Object,
        default(rawProps){
            return {
                title: 'Appointment Title',
                type: 'Appointment Type',
                status: 'scheduled',
                datetime: 'May 2, 2025 · 10:00 AM',
                location: '123 Greenway Blvd',
                employee: {
                    fullName: 'Sarah Johnson',
                    title: 'Senior Engineer'
                }
            }
        }
    }
})
</script>


<template>
<div class="appointment-card upcoming">
    <div class="appointment-header">
        <h2>{{ appointment.title }}</h2>
        <span class="appointment-time">{{ appointment.datetime }}</span>
    </div>
    <div class="appointment-body">
        <p><strong>Location:</strong> {{ appointment.location }}</p>
        <p><strong>Client:</strong> {{ appointment.employee.fullName }}({{ appointment.employee.title }})</p>
        <p><strong>Type:</strong> {{ appointment.type }}</p>
    </div>
    <div class="appointment-footer">
        <div v-if="appointment.status == 'scheduled'">
            <div class="btn-container">
                <button class="reschedule-btn">Reschedule</button>
                <button class="cancel-btn">Cancel</button>
            </div>
        </div>
        <div v-else-if="appointment.status == 'cancelled'">
            <p style="color: var(--color-error)">Appointment Cancelled</p>
            <br>
            <div class="btn-container">
                <button class="reschedule-btn">Reschedule</button>
            </div>
        </div>
    </div>
</div>
</template>

<style scoped lang="scss">
$primary-green: #2e7d32;
$light-green: #81c784;
$past-green: #c8e6c9;
$background-color: #f5f9f6;
$text-color: #4a4a4a;
$muted-text-color: #6b8e6b;
$border-color: #dfe8e2;
$card-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);

$btn-reschedule: #66bb6a;
$btn-reschedule-hover: #5aaa5a;
$btn-cancel: #ef5350;
$btn-cancel-hover: #e53935;
$btn-summary: #4caf50;
$btn-summary-hover: #43a047;


.appointments-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 20px;
}

.appointment-card {
  background: #fff;
  border: 1px solid $border-color;
  border-radius: 16px;
  box-shadow: $card-shadow;
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: transform 0.2s;

  &:hover {
    transform: translateY(-4px);
  }

  &.upcoming {
    border-left: 5px solid $light-green;
  }

  &.past {
    opacity: 0.7;
    border-left: 5px solid $past-green;
  }

  .appointment-header {
    h2 {
      font-size: 1.1rem;
      color: $primary-green;
      margin: 0;
    }

    .appointment-time {
      font-size: 0.9rem;
      color: $muted-text-color;
      margin-top: 4px;
    }
  }

  .appointment-body {
    p {
      margin: 8px 0;
      font-size: 0.95rem;
      color: $text-color;
    }
  }

  .appointment-footer {
        margin-top: 15px;
        .btn-container{
            display: flex;
            justify-content: flex-start;
            gap: 10px;
        }

        button {
            padding: 8px 14px;
            font-size: 0.85rem;
            border: none;
            border-radius: 8px;
            cursor: pointer;

            &.reschedule-btn {
            background-color: $btn-reschedule;
            color: #fff;

            &:hover {
                background-color: $btn-reschedule-hover;
            }
            }

            &.cancel-btn {
            background-color: $btn-cancel;
            color: #fff;

            &:hover {
                background-color: $btn-cancel-hover;
            }
            }

      &.view-summary-btn {
        background-color: $btn-summary;
        color: #fff;

        &:hover {
          background-color: $btn-summary-hover;
        }
      }
    }
  }
}
</style>