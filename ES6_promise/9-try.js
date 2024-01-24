export default function guardrail(mathFunction) {
  const queue = [];
  try {
    // Execute mathFunction and push result to the queue
    const result = mathFunction();
    queue.push(result);
  } catch (error) {
    // Handle any errors that occur during execution
    queue.push(error.message);
  } finally {
    // Push 'Guardrail was processed' to the queue
    queue.push('Guardrail was processed');
  }
  return queue;
}
