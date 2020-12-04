#ifndef NAIVEBAYES_H
#define NAIVEBAYES_H

typedef struct class_summary
{
    std::vector<std::vector<float>> mean_std;
    float prob_class;
} class_summary;

class Naive_Bayes
{
    private: 
        std::vector<float> unique_label;
        std::vector<class_summary> summary;

    public:
        void fit(std::vector<std::vector<float>> dataset);
        int predict(const std::vector<float> &test_data, const class_summary &summary);

};

class_summary get_class_summary(std::vector<std::vector<float>> dataset, float);
#endif
