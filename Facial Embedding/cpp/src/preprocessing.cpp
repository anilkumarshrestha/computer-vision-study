#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include<algorithm>
#include "preprocessing.h"
#include "Math.h"
std::vector<std::vector<float>* > get_embedding_data(std::string file_name)
{
    std::ifstream in_state_(file_name.c_str(), std::ifstream::in);
    std::vector< std::vector<float>* > state_out;
    std::string line;


    while (getline(in_state_, line))
    {
        std::istringstream iss(line);
        std::vector<float>* x_coord = new std::vector<float>();

        std::string token;
    	while( getline(iss,token,','))
    	{
    	    x_coord->push_back(std::stod(token));
    	}
        state_out.push_back(x_coord);
    }
    return state_out;
}

std::vector<float>get_label(std::string file_name)
{
    std::ifstream in_label_(file_name.c_str(), std::ifstream::in);
    std::vector< float> label_out;
    std::string line;
    while (getline(in_label_, line))
    {
        std::istringstream iss(line);
        float label;
	    iss >> label;
            //std::cout<<"type:"<<typeid(label).name()<<std::endl;

	    label_out.push_back(label);
    }
   return label_out;
}


std::vector<std::vector<float>> split_by_class( std::vector<std::vector<float>>& dataset ,float data_class )
{
   std::vector< std::vector<float> > temp_out;
   std::vector< std::vector<float> > out_Vector;
   std::vector<float> temp;
   int counter = 0;
   std::for_each( dataset[4].begin(), dataset[4].end(), [&](float & item_class)
   { 
      if(item_class == data_class )
      {
         std::vector<float> temp;
         temp.push_back(dataset[0][counter]);
         temp.push_back(dataset[1][counter]);
         temp.push_back(dataset[2][counter]);
         temp.push_back(dataset[3][counter]);
         temp.push_back(dataset[4][counter]);
         temp_out.push_back(temp);
      }      
      counter++;
   });
   out_Vector = alg_math::vect_Transpose(temp_out);
   return out_Vector;
}

std::vector<std::vector<float>* > get_train_split(const std::vector<std::vector<float>* > &vect , float percent)
{
   std::vector< std::vector<float>* > temp_out;
   std::vector<std::vector<float>* > input = vect;
   int size = vect[0].size() * percent/100;
   // dealing with data as vectors is easier than separating features in vectors
   input = alg_math::vect_Transpose(input);
   for (auto temp =input.begin() ; temp != input.begin()+ size; temp++ )
   {
      temp_out.push_back(*temp);
   }
   return alg_math::vect_Transpose(temp_out);
}


std::vector<std::vector<float>* > get_test_split( std::vector<std::vector<float>* > &vect , float percent)
{
   std::vector< std::vector<float>* > temp_out;
   std::vector<std::vector<float>* > input = vect;
   int sindex = vect[0].size() * (100 - percent)/100;

   // dealing with data as vectors is easier than separating features in vectors
   input = alg_math::vect_Transpose(input);
   for (auto temp =input.begin()+ sindex ; temp != input.end(); temp++ )
   {
      temp_out.push_back(*temp);
   }
   return alg_math::vect_Transpose(temp_out);
}

float vect_match_score (const std::vector<float> &labels, const std::vector<float> &predictions )
{
    float result=0;
    int index=0;
    std::for_each(labels.begin(), labels.end(), [&](float label)
    {
        if(label == predictions[index])
        {
            result++;
        }
        index++;
    });
    return float(100*result/labels.size());
}
