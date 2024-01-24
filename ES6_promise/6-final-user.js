// Import necessary functions
import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

// Function to handle user profile signup and photo upload
const handleProfileSignup = async (firstName, lastName, fileName) => {
  const result = [];
  try {
    // Sign up the user
    const user = await signUpUser(firstName, lastName);
    result.push({ status: 'fulfilled', value: user });

    // Attempt to upload the photo
    await uploadPhoto(fileName);
  } catch (error) {
    // Handle any errors during signup or photo upload
    result.push({
      status: 'rejected',
      value: error.toString(),
    });
  }
  return result;
};

// Export the handleProfileSignup function
export default handleProfileSignup;
