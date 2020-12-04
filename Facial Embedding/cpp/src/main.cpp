#include <vector>
#include <iostream>
#include "preprocessing.h"
#include "nb.h"
int main()
{
    std::string data_fname = "../../Embeddings/emb.txt";
    std::string label_fname = "../../Embeddings/label.txt";
    std::vector<std::vector<float>* > dataset = get_embedding_data(data_fname);
    std::vector<float> label = get_label(label_fname);

    Naive_Bayes naive = Naive_Bayes();

    std::cout<<"Loading successful."<<std::endl;
    std::cout<<"Data size:"<<dataset.size() << std::endl;
    std::cout << "Label:"<<label.size() << std::endl;

    float p = 80;
    std::vector<std::vector<float>> training_data = get_train_split(dataset, p);
    std::vector<std::vector<float>> test_split = get_test_split(dataset, 100 - p);
    
    naive.fit(training_data);
    
    
    return 0;
}
