// Import utility functions
import { uploadPhoto, createUser } from './utils';

// Function to handle user profile signup
export default function handleProfileSignup() {
  // Execute both uploadPhoto and createUser simultaneously
  return Promise.all([uploadPhoto(), createUser()])
    .then((values) => {
      // Log the result when both promises are successful
      console.log(
        `${values[0].body} ${values[1].firstName} ${values[1].lastName}`,
      );
    })
    // Handle any errors during the signup process
    .catch(() => console.log('Signup system offline'));
}
