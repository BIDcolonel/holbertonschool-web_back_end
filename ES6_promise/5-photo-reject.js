// Function to simulate photo upload
export default function uploadPhoto(filename) {
  // Return a rejected promise with an error message
  return Promise.reject(new Error(`${filename} cannot be processed`));
}
