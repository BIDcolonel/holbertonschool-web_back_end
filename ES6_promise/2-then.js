// Function to handle the response from an API call
export default function handleResponseFromAPI(promise) {
  // Accept a promise as an argument
  return promise
    // If the promise resolves successfully
    .then(() => ({ status: 200, body: 'success' }))
    // If the promise is rejected
    .catch(() => Error())
    // After either resolving or rejecting the promise
    .finally(() => console.log('Got a response from the API'));
}
