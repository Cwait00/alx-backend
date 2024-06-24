import kue from 'kue';

const blacklistedNumbers = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);

  if (blacklistedNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}

const queue = kue.createQueue();

queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});

queue.on('job enqueue', (id, type) => {
  console.log(`Job ${id} got queued of type ${type}`);
}).on('job complete', (id, result) => {
  kue.Job.get(id, (err, job) => {
    if (err) return;
    job.remove((err) => {
      if (err) throw err;
      console.log(`Removed completed job ${id}`);
    });
  });
}).on('job failed', (id, errorMessage) => {
  console.log(`Job ${id} failed with error ${errorMessage}`);
}).on('job progress', (id, progress) => {
  console.log(`Job ${id} ${progress}% complete`);
});
