main_directory='/Users/shivamgoyal/Desktop/Cybersecurity/Project/Deepfake-Audio-Detection-with-XAI/for-rerecorded/'

val_fake='validation/fake'
test_fake='testing/fake'
train_fake='training/fake'

val_real='validation/real'
test_real='testing/real'
train_real='training/real'

spect_directory= main_directory+'spectogram/'
spect_val_directory_fake= spect_directory+ val_fake
spect_val_directory_real= spect_directory+ val_real

spect_test_directory_fake= spect_directory+test_fake
spect_test_directory_real= spect_directory+test_real

spect_train_directory_fake= spect_directory+ train_fake
spect_train_directory_real= spect_directory+ train_real

input_val_path_fake = main_directory+ val_fake
input_val_path_real = main_directory+ val_real

input_test_path_real= main_directory + test_real
input_test_path_fake= main_directory + test_fake

input_train_path_real= main_directory + train_real
input_train_path_fake= main_directory + train_fake
# print(input_train_path_fake)
# print(input_train_path_real)
# print(spect_train_directory_fake)
# print(spect_train_directory_real)