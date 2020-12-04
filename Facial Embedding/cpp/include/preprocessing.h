#include <iostream>

std::vector<std::vector<float>> get_embedding_data(std::string);
std::vector<float> get_label(std::string);
#ifndef PREPROCESSING_H
#define PREPROCESSING_H

std::vector<std::vector<float>> get_embedding_data(std::string);
std::vector<std::vector<float>> split_by_class( std::vector<std::vector<float>> &dataset ,float data_class );
std::vector<std::vector<float>> get_train_split(const std::vector<std::vector<float>> &vect , float percent);
std::vector<std::vector<float>> get_test_split(std::vector<std::vector<float>> &vect , float percent);
float vect_match_score (const std::vector<float> &labels, const std::vector<float> &predictions );
#endif
