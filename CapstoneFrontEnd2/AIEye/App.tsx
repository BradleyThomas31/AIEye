import React, { useState } from 'react';
import { Image, TouchableOpacity, StyleSheet, Text, View, TextInput } from 'react-native';
import { launchCamera, launchImageLibrary } from 'react-native-image-picker';


function App(): React.JSX.Element {
  const [inputText, setInputText] = useState('');
  const [imageUri, setImageUri] = useState('');
  const [serverResponse, setServerResponse] = useState('');

function callFlaskServer() {
  fetch('http://127.0.0.1:5000', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      inputText: inputText,  
    }),
  })
  .then(response => response.json()) 
  .then(data => {
    console.log(data.response); 
    setServerResponse(data.response); 
  })
  .catch(error => {
    console.error('There was an error!', error);
  });
}


  function loadLibrary() {
    launchImageLibrary({}, (response) => {
      if (response.assets && response.assets.length > 0) {
        setImageUri(response.assets[0].uri);
        console.log(response.assets[0].uri); 
      }
    });
  }

  function loadCamera() {
    launchCamera({}, (response) => {
      if (response.assets && response.assets.length > 0) {
        setImageUri(response.assets[0].uri);
        console.log(response.assets[0].uri); 
      }
    });
  }

  return (
    <View style={styles.mainContainer}>
      <View style={styles.buttonContainer}>
        <TouchableOpacity onPress={loadLibrary}>
          <Text>Upload a photo</Text>
        </TouchableOpacity>
        <TouchableOpacity onPress={loadCamera}>
          <Text>Take a photo</Text>
        </TouchableOpacity>
      </View>
      {imageUri ? (
        <Image
          source={{ uri: imageUri }}
          style={styles.image}
        />
      ) : null}
      <TextInput
        style={styles.input}
        placeholder="Enter your question"
        onChangeText={setInputText}
        value={inputText}
      />
<TouchableOpacity onPress={callFlaskServer}>
  <Text>Call Flask Server</Text>
</TouchableOpacity>
<Text>Server Response: {serverResponse}</Text>

    </View>
  );
}

// Updated Styles
const styles = StyleSheet.create({
  mainContainer: {
    flex: 1,
    justifyContent: 'space-around', 
    alignItems: 'center',
    backgroundColor: '#fff',
  },
  buttonContainer: {
    flexDirection: 'row', 
    justifyContent: 'space-around',
    width: '100%', 
  },
  input: {
    height: 40,
    margin: 12,
    borderWidth: 1,
    padding: 10,
    width: '80%',
  },
  image: {
    width: 200, 
    height: 200,
    resizeMode: 'contain', 
  },
});

export default App;

