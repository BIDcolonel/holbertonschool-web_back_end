export default function guardrail(mathFunction) {
  const queue = [];
  try {
    // Push 'Math ran successfully' to the queue
    queue.push(mathFunction());
  } catch (error) {
    // Push 'Error: ' followed by the error message to the queue
    queue.push(`Error: ${error.message}`);
  }
  // Push 'Guardrail was processed' to the queue
  queue.push('Guardrail was processed');
  return queue;
}
