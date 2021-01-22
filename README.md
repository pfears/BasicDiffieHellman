# BasicDiffieHellman
Super Basic Implementation of Diffie-Hellman Encryption 

This script shows the simple interaction of how two Person objects (Bob and Alice) can interact "Securely" with one another using Diffie-Hellman Encryption.

Who Knows What:
  1) Public Knowledge: Base and Modulus
  2) Bob's Knowledge: Bob's secret key and Public Knowledge
  3) Alice's Knowledge: Alice's secret key and Public Knowledge

Steps To Encryption:
  1) Bob and Alice pubicly decide the value for the Base and Modulus
  2) Bob raises the publicly known Base to the value of his Secret Key and then takes the publicly known Modulus of the calculated number to create his Partial Key
  3) Bob sends his Partial Key to Alice
  4) Alice performs the same action with her Secret Key, and takes the publicly known Modululs of the calculated number to create her Partial Key
  5) Alice sends her Partial Key to Bob
  6) Bob receives Alice's Partial Key, first he raises it to the power of his Secret Key, then he takes the publicly known Modulus, allowing him to calculate the Full Key
  7) Alice receives Bob's Partial Key and performs the same actions, granting her with the same Full Key
  
  
Steps To Decryption:
  1) Take the Encrypted Number (referenced as T below) and subtract it from the Full Key (referenced as X below), then take the Modulus (referenced as M below) of the difference
    Example: (T - X) mod M
    
