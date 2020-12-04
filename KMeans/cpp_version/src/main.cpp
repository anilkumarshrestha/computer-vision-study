#include<iostream>
#include<vector>
#include<fstream>
using namespace std;

int ReverseInt (int i)
{
    unsigned char ch1, ch2, ch3, ch4;
    ch1 = i & 255;
    ch2 = (i >> 8) & 255;
    ch3 = (i >> 16) & 255;
    ch4 = (i >> 24) & 255;
    return((int) ch1 << 24) + ((int)ch2 << 16) + ((int)ch3 << 8) + ch4;
}

void read_Mnist(string filename, vector<vector<double> > &vec)
{
    ifstream file (filename, ios::binary);
    if (file.is_open())
    {
        int magic_number = 0;
        int number_of_images = 0;
        int n_rows = 0;
        int n_cols = 0;
        file.read((char*) &magic_number, sizeof(magic_number));
        magic_number = ReverseInt(magic_number);
        cout << magic_number << endl;
        file.read((char*) &number_of_images,sizeof(number_of_images));
        number_of_images = ReverseInt(number_of_images);
        file.read((char*) &n_rows, sizeof(n_rows));
        n_rows = ReverseInt(n_rows);
        file.read((char*) &n_cols, sizeof(n_cols));
        n_cols = ReverseInt(n_cols);
        cout << "r = " << n_rows << "    col = "<< n_cols << endl;
        for(int i = 0; i < number_of_images; ++i)
        {
            vector<double> tp;
            for(int r = 0; r < n_rows; ++r)
            {
                for(int c = 0; c < n_cols; ++c)
                {
                    unsigned char temp = 0;
                    file.read((char*) &temp, sizeof(temp));
                    // cout << temp << " | ";
                    tp.push_back((double)temp);
                }
            }
            vec.push_back(tp);
        }
    }
}

void read_Mnist_Label(string filename, vector<double> &vec)
{
    ifstream file (filename, ios::binary);
    if (file.is_open())
    {
        int magic_number = 0;
        int number_of_images = 0;
        int n_rows = 0;
        int n_cols = 0;
        file.read((char*) &magic_number, sizeof(magic_number));
        magic_number = ReverseInt(magic_number);
        file.read((char*) &number_of_images,sizeof(number_of_images));
        number_of_images = ReverseInt(number_of_images);
        for(int i = 0; i < number_of_images; ++i)
        {
            unsigned char temp = 0;
            file.read((char*) &temp, sizeof(temp));
            vec[i]= (double)temp;
        }
    }
}


// void read_Mnist(string filename, vector<cv::Mat> &vec){
//     ifstream file (filename, ios::binary);
//     if (file.is_open())
//     {
//         int magic_number = 0;
//         int number_of_images = 0;
//         int n_rows = 0;
//         int n_cols = 0;
//         file.read((char*) &magic_number, sizeof(magic_number));
//         magic_number = ReverseInt(magic_number);
//         file.read((char*) &number_of_images,sizeof(number_of_images));
//         number_of_images = ReverseInt(number_of_images);
//         file.read((char*) &n_rows, sizeof(n_rows));
//         n_rows = ReverseInt(n_rows);
//         file.read((char*) &n_cols, sizeof(n_cols));
//         n_cols = ReverseInt(n_cols);
//         for(int i = 0; i < number_of_images; ++i)
//         {
//             cv::Mat tp = Mat::zeros(n_rows, n_cols, CV_8UC1);
//             for(int r = 0; r < n_rows; ++r)
//             {
//                 for(int c = 0; c < n_cols; ++c)
//                 {
//                     unsigned char temp = 0;
//                     file.read((char*) &temp, sizeof(temp));
//                     tp.at<uchar>(r, c) = (int) temp;
//                 }
//             }
//             vec.push_back(tp);
//         }
//     }
// }

class KMeans{
    private:
        int no_clusters;
        int max_itr;
        void KMeans(int n_c, int m_i)
        {
            no_clusters = n_c;
            max_itr = m_i;
        }
    public:
        void run(vector< vector<double> >&);
}


void KMeans::run(vector< vector<double> >& t_data)
{
    //Initializing Clusters
    vector<int> used_pointIds;

    for(int i=1; i<=no_clusters; i++)
    {
        while(true)
        {
            int index = rand() % total_points;

            if(find(used_pointIds.begin(), used_pointIds.end(), index) == used_pointIds.end())
            {
                used_pointIds.push_back(index);
                all_points[index].setCluster(i);
                Cluster cluster(i, all_points[index]);
                clusters.push_back(cluster);
                break;
            }
        }
    }
    cout<<"Clusters initialized = "<<clusters.size()<<endl<<endl;
}


int main()
{

    string train_image_file = "../../data/train-images.idx3-ubyte";
    string train_label_file = "../../data/train-labels.idx1-ubyte";

    int number_of_images = 60000;
    int image_size = 28 * 28;

    vector<vector<double> > train_image;
    read_Mnist(train_image_file, train_image);
    cout<<train_image.size()<<endl;
    cout<<train_image[0].size()<<endl;

    // for (int i = 0; i < 10; i++)
    // {
    //     for (int j= 0; j < 10; j++)
    //     {
    //         cout << " | ";
    //         // cout << typeid(train_image[i][i]).name();
    //         cout << train_image[i][j];
    //     }
        

    // }

    //read MNIST label into double vector
    // vector<double> train_label(number_of_images);
    // read_Mnist_Label(train_label_file, train_label);
    // cout<<train_label.size()<<endl;




    return 0;
}
