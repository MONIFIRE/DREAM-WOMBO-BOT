const login = require("fb-lnw-api-sck");
const fs = require('fs');

// Login to Facebook
login({appState: JSON.parse(fs.readFileSync('cookies.json', 'utf8'))}, (err, api) => {
  if (err) return console.error(err);

  // Listen for incoming messages
  api.listen((err, message) => {
  if (err) return console.error(err);
  if (!message || !message.body) return; // Add this check

  // Check if the message starts with !WOMBO
  if (message.body.startsWith('!WOMBO')) {
    // Extract the user's message
    const userMessage = message.body.slice(7);

    // Write the user's message to a text file
    fs.writeFile('wombo.txt', userMessage, { encoding: 'utf8' }, (err) => {
      if (err) return console.error(err);
      console.log('The file has been saved!');
      api.setMessageReaction(":thumbsup:", message.messageID);
      api.sendMessage({body: 'Loading ..',}, message.threadID);
    });

      // Run the main.py file
      const { spawn } = require('child_process');

      const pythonProcess = spawn('python.exe', ['C:\\Users\\Administrator\\Desktop\\WOBMO\\main.py']);
      
      pythonProcess.stdout.on('data', (data) => {
        console.log(`stdout: ${data}`);
      });
      
      pythonProcess.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
      });
      
      pythonProcess.on('close', (code) => {
        console.log(`child process exited with code ${code}`);
      });
      

      // Send an image to the user
      setTimeout(function() {
        // Send an image to the user
        api.sendMessage({
          attachment: fs.createReadStream('./dream.png')
        }, message.threadID);
      },120000);
    }
  });

});


