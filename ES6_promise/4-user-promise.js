// Function to sign up a user
export default function signUpUser(firstName, lastName) {
  // Return a resolved promise with user's first and last name
  return Promise.resolve({
    firstName,
    lastName,
  });
}
