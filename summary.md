Cryptography I
==============

Cryptography is an indispensable tool for protecting information in computer systems. This course explains the inner workings of cryptographic primitives and how to correctly use them. Students will learn how to reason about the security of cryptographic constructions and how to apply this knowledge to real-world applications. [More ...](https://class.coursera.org/crypto-010/wiki/Overview)
Mật mã là một công cụ không thể thiếu để bảo vệ thông tin trong hệ thống máy tính. Khóa học này giải thích các hoạt động bên trong của mật mã gốc và cách sử dụng chúng một cách chính xác. Học sinh sẽ học cách lập luận về tính bảo mật của các cấu trúc mật mã và cách áp dụng kiến thức này vào các ứng dụng trong thế giới thực.
## Week 1

This week's topic is an overview of what cryptography is about as well as our first example ciphers. You will learn about pseudo-randomness and how to use it for encryption. We will also look at a few basic definitions of secure encryption.
Chủ đề của tuần này là tổng quan về mật mã học cũng như các mật mã ví dụ đầu tiên của chúng tôi. Bạn sẽ tìm hiểu về giả ngẫu nhiên và cách sử dụng nó để mã hóa. Chúng ta cũng sẽ xem xét một vài định nghĩa cơ bản về mã hóa an toàn.
#### Introduction

* HTTPS, SSL/TLS, encrypted disks (mã hóa ổ ứng)
* Symmetric encryption: __E(k,m) = c__, __D(k,c) = m__ (mã đối xứng)
* Crypto core: secret key establishment and secure communication (thiết lập khóa bí mật và liên lạc an toàn)
  * Diffie-Hellman protocol:
    1. Key Generation: Each party generates a public/private key pair. The public key is made publicly available, while the private key is kept secret.

    2. Key Exchange: The parties exchange their public keys over an insecure communication channel.

    3. Shared Secret Generation: Each party uses their private key and the other party's public key to calculate a shared secret. The shared secret is used as the basis for the shared secret key that will be used for encryption and decryption.
   
* Digital signatures, anonymous communication, digital cash (chữ ký số, giao tiếp ẩn danh, tiền ký thuật số)
  * Digital signatures:
    1. Key Generation: The signer generates a pair of public and private keys, with the private key being kept secret.
    2. Hashing: The signer applies a cryptographic hash function to the message to be signed, creating a fixed-length hash value.
    3. Signing: The signer uses their private key to encrypt the hash value, creating the digital signature.
    4. Verification: The recipient of the signed message applies the same hash function to the received message and uses the signer's public key to decrypt the signature. If the decrypted signature matches the calculated hash value, the recipient can trust that the message is authentic and has not been tampered with.
  * Anonymous communication: pseudonyms, hiding IP addresses, encrypting messages, and routing communication through intermediary nodes
  * Digital cash:
* _Substitution Cipher_, _Caesar Cipher_, how to break it by using frequency of English letters, diagrams, triagrams, etc. (mật mã thay thế, mã caesar, cách phá)
* _Vigener cipher_ using secret word, rotor machines, the Enigma (3-5 rotors) (mã Vigener)
* Data encryption standards -- __DES, 3DES, AES, Salsa20__ (các tiêu chuẩn mã hóa)
* Probability distribution, uniform distribution, point distribution, _The Union Bound_, random variable, uniform random variable, randomized algorithm (phân phối chuẩn, phân phối đều, phân phối điểm,, không gian vũ trụ, biến ngẫu nhiên, biến ngẫu nhiên đều, thuật toán ngẫu nhiên)
* Event independence, independent random variables (sự kiện độc lập, biến ngẫu nhiên độc lập)
* __XOR__ preserves uniform randomness (toán tử XOR bảo tồn tính ngẫu nhiên thống nhất)
* The birthday paradox (nghịch lý ngày sinh nhật)

#### Stream Ciphers (mã hóa dòng)

* Symmetric Ciphers (mã đối xứng): a pair of efficient algorithms (sử dụng một cặp thuật toán mã hóa và giải mã) __E: K x M -> C__ and __D: K x C -> M__
* __OTP__ (One Time Pad) -- very fast, long keys, secure cipher (one time pad, dùng khóa 1 lần)
* Secure cipher: cipher text (CT) should reveal nothing about the plain text (PT) (bản mã không chứa thông tin gì về bản rõ)
* Perfect secrecy, but theorem says key length must be equal or greater than message length (an toàn tuyệt đối, nhưng định lý nói rằng, độ dài khóa phải bằng hoặc lớn hơn độ dài bản rõ)
* Stream ciphers -- make OTP practical by replacing random key with pseudorandom key, can not have perfect secrecy (mã hóa dòng, làm cho OTP trở nên thực thế bằng cách dùng khóa giả ngẫu nhiên thay vì ngẫu nhiên => không thể có an toàn tuyệt đối)
* PRG must be unpredictable (thuật toán giả ngẫu nhiên phải không đoán trước được)
* Negligible vs. non-negligible, is a scalar _e_ (không đáng kẻ và đáng kể)
* PRGs are parameterized by a security parameter _lambda_ (thuật toán giả ngẫu nhiên được truyển bởi một tham số bảo mật)
* PRG is predictable at position _i_ if ... (PRG có thể đoán được nếu tồn tại thuật toán A mà ...)
* Two Time Pad is insecure, 802.11b WEP (Two Time Pad thì không an toàn)
* Never use stream cipher key more than once (không bao giờ dùng khóa cho mã hóa dòng nhiều hơn 1 lần)
* OTP does not protect the integrity of the message (malleable), modifications are undetectable but may have predictable impact (OTP không bảo vệ tính toàn vẹn của tin nhawnsm không thể phát hiện được các sửa đổi nhưng có thể có tác động dự đoán được)
* Real world ciphers -- __RC4__, __CSS__ (Các mật mã trong thực tế)
* eStream: seed x nonce -> key
* Is Salsa20 secure -- unknown, no known attacks better than exhaustive search
* Statistical test, advantage of
* PRG is secure if the advantage of all efficient statistical tests is negligible
* Secure PRG is unpredictable, unpredictable PRG is secure
* Two distributions are indistinguishable is no efficient statistical test has advantage greater than negligible
* Semantic security -- two experiments EXP(0) and EXP(1), challenger and adversary, secure if advantage of adversary is negligible
* OTP is semantically secure against __all__ adversaries because it is perfectly secure
* Stream cipher derived from secure PRG is semantically secure

## Week 2

In week 2 we introduce a new primitive called a block cipher that will let us build more powerful forms of encryption. We will look at a few classic block-cipher constructions (3DES and AES) and see how to use them for encryption. Block ciphers are the work horse of cryptography and have many applications. Next week we will see how to use block ciphers to provide data integrity.   

#### Block ciphers

* Block ciphers built by iteration, Round function R(k,m), 3DES -> n=48, AES -> n=10, slower than stream ciphers
* __3DES__ -- n=64 bits, k=168 bits,__AES__ -- n=128 bits, k=128/192/256 bits
* Pseudo Random Function _PRF_ F: K x X -> Y, efficient
* Pseudo Random Permutation _PRP_ F: K x X -> X, efficient, one-to-one, must have inversion algorithm
* Any PRP is also PRF
* Secure PRF -- indistinguishable from random function
* Secure PRP -- indistinguishable from random function
* Easy application: PRF -> PRG
* DES core idea -- Feistel network, S-boxes, P-boxes
* __Luby-Rackoff (85) Theorem__ -- 3-Round Feistel network is a secure PRP
* Exhaustive search attacks, DES challenge - 56 bits ciphers should not be used
* 3DES -- 3E( K1,K2,K3, M ) = E( K1, D( K2, E( K3, M ))), 3 times slower than DES
* Why not double DES -- meet in the double attack, key space reduced to 2 ** 56 
* More attacks on block ciphers
* __AES is Subs-Perm network__, not Feistel -- Round function is ByteSub, ShiftRow, MixColumn
* Block cipher from PRG -- extending a PRG

#### Using block ciphers

* Secure PRF, if for all efficient A, Adv( A,F ) is negligible
* PRF Switching Lemma -- every secure PRP is secure PRF if |X| is sufficiently large
* Mode of operation -- one time key (the adversary sees only one ciphertext)
* Incorrect: __Electronic Code Block (ECB)__ is not semantically secure
* Deterministic Counter Mode -- make stream cipher out of block cipher
* Mode of operation -- security for many-time key (the adversary can obtain ciphertext of arbitrary messages of his choice)
* If secret key is to be used many times => given the same plaintext twice encryption must produce different outputs
* Solution 1: randomized encryption
* Solution 2: nonce-based encryption -- 1) nonce is a counter, 2) nonce is random chosen by encryptor
* Mode of operation -- __many-time key (CBC)__, CBC Theorem -- if E is secure PRP then E-CBC is semantically secure under CPA
* CBC where attacker can predict IV is not CPA-secure 
* Nonce-based CBC, key = (K,K1) to encrypt nonce
* Mode of operation -- __many-time key (CTR)__, randomized counter-mode, parallelizable
* IV chose at random with every message, needs only PRF not PRP, never decrypted?
* Neither mode ensures data integrity

## Week 3

This week's topic is data integrity and we will discuss a number of classic constructions for MAC systems. For now we only discuss how to prevent modification of non-secret data.

#### Message integrity

* Goal is to protect integrity not to assure confidentiality, requires secret key
* MAC is a pair of algirithms S(k,m) -> t and V(k,m,t) -> _yes_ or _no_
* Secure MACs prevent _existential forgery_ -- attacker can not produce some new valid message/tag pair
* MAC is Secure if for all _efficient_ algorithms A the advantage of attacker is negligible 
* Secure PRF makes Secure MAC if |Y| is sufficiently large (say 2**80)
* How to convert Small-MAC to a Big-MAC -- __CBC-MAC__ (banking) and __HMAC__ (Internet protocols)
* Truncating MAC based on PRF is a secure PRF
* __CBC-MAC__ -- encrypted and nested variants, need 2 keys; _NCBC-MAC_ not used with _AES_ or _3DES_ but used with _HMAC_
* _CBC-MAC_ padding
* PMAC and Carter-Wegman MAC to parallelize MAC execution, CW( (k1,k2),m ) = (r, F(k1,r) ⊕ S(k2,m) )
* CW -- randomized MAC built from a fast one-time MAC
* PMAC is incremental, the tag can be updated if only a portion of the message has changed
* If (S,V) is a secure one-time MAC and Fa secure PRF then Carter-Wegman is secure MAC

#### Collision Resistance

* If I=(S(k,H(m)),V(k,H(m),t)) is secure MAC and H is collision-resistant hash function then I-big is secure MAC
* Collision resistance (CR) is necessary for security
* The birthday paradox: when n = 1.2 x sqrt(B) then P(collision) > 1/2
* Therefore generic attack requires O(2 ^ n/2) time and space O(2 ^ n/2)
* CR has functions -- SHA-1, SHA-256, SHA-512
* __Merkel-Damgard construction__ -- given CR function for short messages, create CR function for long messages
* __Davies-Meyer__ compression function -- h(H,m) = E(m,H) ⊕ H where E is ideal cipher
* Not CR function -- h(H,m) = E(m,H)
* __SHA-256__: Merkel-Damgard function, Davies-Meyer compression function, block cipher SHACAL-2
* __HMAC__: building a MAC out of hash function
* HMAC: S(k,m) = H( k⊕opad || H( k⊕ipad || m ))
* Timing attacks on MAC verification

## Week 4

This week's topic is authenticated encryption: encryption methods that ensure both confidentiality and integrity. We will also discuss a few odds and ends such as how to search on encrypted data. This is our last week studying symmetric encryption. Next week we start with key management and public-key cryptography.

#### Authenticated Encryption

* Encryption that is secure against _tampering_, ensuring both confidentiality and integrity -- authenticated encryption (introduced ca 2000)
* CBC with random IV -- attacker can modify the data w/o decrypting it
* CPA security can not guarantee secrecy under active attacks
* Cipher (E,D) where E: K x M x N -> C but D: K x C x N -> M or _bottom_
* Cipher (E,D) provides authenticated encryption (AE) if it is semantically secure under CPA and has ciphertext integrity
* _Chosen ciphertext security_
* Cipher that provides AE is CCA secure
* Note 1) AE does not prevent replay attacks and 2) does not account for side channels (timing)
* Combining MAC and ENC
 * SSL: MAC-then-Encrypt may be insecure against CCA attacks but when (E,D) is rand-CTR mode or rand-CDC then provides AE
 * IPSec: Encrypt-then-MAC always provides AE
 * SSH: Encrypt-and-MAC
* OCB -- more efficient AE, one encryption per block
* TLS record protocol (TLS 1.2) -- unidirectional keys, two 64-bit counters for each side (init 0) for replay defense
* Bugs in TLS 1.1 -- 1) _IV for CBC is predictable_ 2) _Padding Oracle_
* The TLS headers leaks the length of TLS records

#### Odds and ends

* A single source key (SK) is sampled from 1) hardware rng, or 2) key exchange protocol
* Need many keys to secure session -- unidirectional keys, multiple keys for nonce-based CBC
* __KDF__ -- generate many keys from single source key, KDF( SK, CTX, L ) := F( SK, (CTX||0)) || F( SK, (CTX||1)) || ...
* CTX -- a string that uniquely identifies the application
* What if source is not uniform -- __Extract-then-Expand__ paradigm (using salt)
* __HKDF__: a KDF from HMAC
* Extract -- HMAC( salt, SK) -> k
* Then expand using HMAC as a PRF with key k
* Deriving keys from password -- do not use HKDF because of low enthropy, vulnerable to dictionary attacks
* PBKDF defence -- salt and _slow hash function_, standard approach __PKCS#5__
* Deterministic encryption (no nonce), but attacker can tell when two ciphertexts encrypt the same message
* A solution -- the case of unique messages
* __Synthetic IV (SIV)__: Deterministic AE, F( k1,m ) -> r, E( k2, m, r ) -> c
* _EME_ -- constructing a wide block PRP, performance can be 2 times slower than SIV
* Disk encryption -- encryption can not expand plaintext (M=C), must use deterministic encryption, no integrity, every sector needs to be encrypted with a PRP
* Tweakable encryption -- construct many PRPs from a key k
* __XTS tweakable block cipher__
* Format preserving encryption (FPE) for encrypting credit card numbers

## Week 5

Basic key exchange: how to setup a secret key between two parties. For now we only consider protocols secure against eavesdropping. This question motivates the main concepts of public key cryptography, but before we build public key systems we need to take a brief detour and cover a few basic concepts from computational number theory. We will start with algorithms dating back to antiquity (Euclid) and work our way up to Fermat, Euler, and Legendre. We will also mention in passing a few useful concepts from 20th century math.

#### Basic key exchange: Trusted 3rd parties

* Problem: storing mutual secret keys is difficult
* __TTP__ -- Online Trusted 3rd Party; eavesdropping security only, insecure against replay, basis of __Kerberos__ 
* Generate keys without TTP -- Merkel puzzles (1974), Diffie-Hellman (1976), RSA (1977)
* _Merkel puzzles_: very inefficient, puzzle(P) = E(P, "message"), where P=0^96||k32, attacker spends quadratic time to break the security
* _Diffie-Hellman_ protocol: fix large prime number p and integer g, g^a (mod p) and g^b(mod p), k=g^(a*b), requires very large key size
* Slow transition away from DH to elliptic curves
* Insecure against Man-In-The-Middle (MiTM) attack, 2 parties can immediately communicate securely, even 3 parties, 4 and more unknown
* Public-key encryption system is triple of algorithms G -- randomized alg. outputs (pk,sk), E(pk,m) -> c -- randomized alg. takes m outputs c, D(sk,c) -> m -- deterministic alg. that takes c outputs м ор nil
* Consistency -- for every (pk,sk) output by G, D( sk, E(pk,m)) = m
* Semantic security, vulnerable to MiTM
* Construction rely on hard problems from number theory and algebra

#### Introduction to Number Theory

* Modular arithmetic, Zn, gcd(x,y) = a*x + b*y (there exist a,b such that...), x and y are relatively prime if gcd(x,y)=1
* Modular inversion x*y = 1 in Zn, x has inverse in Zn iff gcd(x,N)=1
* Zn-star -- set of invertible elements in Zn
* Solving modular linear equations: a*x + b = 0 in Zn => x = -b * a^-1, find a^-1 in Zn using extended Euclid in O(log^2(n))
* _Fermat's theorem_ -- for every x in Zp-start, x^(p-1) = 1 in Zp
* Application: generating large random primes 
* Zp-star is a cyclic group, that is there is generator g such that { 1, g, g^2, g^3, ... , g^(p-2) } = Zp-star, not every element is generator
* The order of g, ord(g) is the size of <g>
* _Lagrange theorem_ -- ord(g) divides p-1
* Euler's generalization of Fermat's theorem: for every x in Zn-star x^fi(N) = 1 in Zn
* Modular e'th root: x^e = c is called e'th root of c
* Arithmetic algorithms: given 2 n-bits integer, we can add and subtract in O(n), multiplication in better than O(n^2), division with reminder O(n^2)
* Exponentiation: _repeated squaring algorithm_
* Intractable problems: 

## Week 6

This week's topic is public key encryption: how to encrypt using a public key and decrypt using a secret key. Public key encryption is used for session setup in HTTPS, for key management in encrypted file systems, and for many other tasks. We will see how to use public-key encryption in the video segments.

### Public Key Encryption from trapdoor permutations

* _Public-key Encryption System_ is triple of algorithms (G, E, D), where G() is randomized alg. that outputs a key pair (pk,sk), E(pk,m) is randomized alg. that takes _m' and outputs 'c', and D(sk,c) is deterministic alg. that takes _c_ and outputs _m_
* Consistency: for every (pk,sk) output by G: for every m: D*sk, E(pk,m)) = m
* Security against eavesdropping, many-time security (follows from fact that attacker can encrypt by himself), Public key encryption _must_ be randomized
* Chosen Ciphertext Security (CCA) -- phase 1, challenge, phase2
* Active attacks: symmetric vs. pub-key => chose plaintext security & ciphertext integrity vs. chosen ciphertext security
* Pub-key Encryption construction -- trapdoor function X -> Y is a tripple of efficient algorithms (G, F, F-1)
* Secure Trapdoor Functions (TDFs) if F(pk,m) can be evaluated but can not be inverted without sk
* Pub-key encryption from TDFs: secure TDF, symmetric auth. encryption, H: X->K a hash function
* Incorrect use of TDF -- never encrypt by applying F directly to plaintext -- deterministic therefore cannot be semantically secure!
* RSA trapdoor permutation -- choose random primes p,q (about 1024 bits), set N=p*q, choose integers e,d such that e*d=1 mod phi(N), output pk=(N,e), sk=(N,d), F=RSA(x)=x^e (in Zn), F-1(sk,y)=y^d
* RSA assumption: RSA is one-way permutation
* Textbook RSA is insecure!!! Is not semantically secure and many attacks exist
* PKCS 1, version 1.5, mode 2
* Attack on PKCS1 v1.5 -- Bleichenbacher 1998, can be avoided by treating incorrectly formatted message blocks in a manner indistinguishable from correctly formatted RSA blocks
* PKCS1 v2.0 OAEP -- is CCA secure when H,g are _random oracles_, in practice use SHA-256 for H and G
* Is RSA a one-way permutation? How not to improve RSA performance?
* RSA with low public exponenent, minimum value e=3, recommended e=65537=2^16+1

### Public key encryption from Diffie-Hellman

* ElGamal Public-key System, based on Diffie-hellman protocol, goal is chose ciphertext security
* Fix a finite cycle group G=(Zp)-star of order n, fix a generator g in G, Alice => choose a in {1..n}, A=g^a is treated as public key, Bob => choose random b in {1..n}, to decrypt -- compute g^(a*b)=B^a, derive k, and decrypt
* Computational Diffie-Hellman Assumption (CDH) holds in G if: known g, g^a, g^b but can not compute g^(a*b)
* Hash Diffie-Hellman Assumption
* ElGamal is semantically secure under Hash-DH
* ElGamal chosen ciphertext security -- if Interactive Diffie-Hellman (IDH) holds in the group G then (Es, Ds) provides authenticated encryption
* ElGamal variants -- twin ElGamal, ElGamal security w/o random oracles
* Many more topics -- Elliptic Curve Crypto, Quantum computing, identity-based encryption and functional encryption, Anonymous digital cash, private voting and auction systems, fully homomorphic encryption, Lattice-based crypto, two-party and multi-party computation, 

