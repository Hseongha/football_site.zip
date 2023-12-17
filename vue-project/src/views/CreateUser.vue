<template>
  <div class="create-user">
    <h1>사용자 생성</h1>
    <form @submit.prevent="submitForm" class="user-form">
      <div class="form-group">
        <label for="name">Name:</label>
        <input type="text" id="name" v-model="user.name" required class="form-control">
      </div>
      
      <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="user.password" required class="form-control">
      </div>
      
      <div class="form-group">
        <label for="gender">Gender:</label>
        <select id="gender" v-model="user.gender" required class="form-control">
          <option value="male">Male</option>
          <option value="female">Female</option>
        </select>
      </div>
      
      <div class="form-group">
        <label for="age">Age:</label>
        <input type="number" id="age" v-model="user.age" required class="form-control">
      </div>
      
      <button type="submit" class="btn btn-primary">Create User</button>
    </form>
    <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
    <p v-if="successMessage" class="success-message">{{ successMessage }}</p>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

export default {
  name: 'CreateUser',
  setup() {
    const user = ref({
      name: '',
      password: '',
      gender: 'male',
      age: 0
    });

    const errorMessage = ref('');
    const successMessage = ref('');

    const router = useRouter();
    const submitForm = async () => {
      try {
        const response = await fetch('http://localhost:5000/create_user', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(user.value)
        });

        if (response.status === 201) {
          successMessage.value = 'User created successfully';
          errorMessage.value = '';
          router.push('/GetAllUsers');
        } else {
          errorMessage.value = 'Failed to create user';
          successMessage.value = '';
        }
      } catch (error) {
        errorMessage.value = 'An error occurred';
        successMessage.value = '';
        console.error('An error occurred:', error);
      }
    };

    return {
      user,
      submitForm,
      errorMessage,
      successMessage
    };
  }
};
</script>

<style>
.create-user {
  max-width: 300px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.user-form .form-group {
  margin-bottom: 15px;
}

.error-message {
  color: red;
  margin-top: 10px;
}

.success-message {
  color: green;
  margin-top: 10px;
}
</style>
