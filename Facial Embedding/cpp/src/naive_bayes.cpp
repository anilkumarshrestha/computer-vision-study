#include<vector>
#include "preprocessing.h"
#include "nb.h"
#include <algorithm>
#include "Math.h"
void Naive_Bayes::fit(std::vector<std::vector <float>> training_data)
{
    unique_label = training_data[training_data.size()-1];
    std::sort(unique_label.begin(), unique_label.end());
    unique_label.erase(std::unique(unique_label.begin(), unique_label.end()), unique_label.end());

    for(auto row = unique_label.begin(); row != unique_label.end(); row++)
    {
        summary.push_back( get_class_summary(training_data, *row));
    }
}


class_summary get_class_summary(std::vector<std::vector<float>> dataset, float class_label)
{
    auto class_data = split_by_class(dataset, class_label);
    class_summary summary;
    std::vector<float> temp;
    for(auto row = class_data.begin(); row != class_data.end()-1; row++)
    {
        temp.clear();
        temp.push_back(alg_math::Math_Mean(*row));
        temp.push_back(alg_math::Math_Var(*row));
        summary.mean_std.push_back(temp);
    }
    
    summary.prob_class = float(class_data[0].size()) / dataset[0].size();
    return summary;

}


