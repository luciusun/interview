// main.cpp
// 维特比解码，将python代码翻译得出，https://www.github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/crf/python/ops/crf.py

#include <iostream>
#include <string>
#include<cmath>
#include <stack>
#include <vector>

using namespace std;

//取二维矩阵的某一行
std::vector<float> GetMatrixLine(std::vector<std::vector<float>> matrix, int line){
    std::vector<float> one_line(matrix[0].size());

    //取出一行处理
    for(int j=0;j<matrix[line].size();j++)
    {
        one_line[j] = matrix[line][j];
    }

    return one_line;

}

std::vector<int> GetMatrixLineInt(std::vector<std::vector<int>> matrix, int line){
    std::vector<int> one_line(matrix[0].size());

    //取出一行处理
    for(int j=0;j<matrix[line].size();j++)
    {
        one_line[j] = matrix[line][j];
    }

    return one_line;

}

//取二维矩阵的某一列
std::vector<float> GetMatrixColumn(std::vector<std::vector<float>> matrix, int column){
    std::vector<float> one_line(matrix[0].size());

    //取出一列处理
    for(int j=0;j<matrix[0].size();j++)
    {
        one_line[j] = matrix[j][column];
    }

    return one_line;

}


//一维数组转化为二维数组
std::vector<std::vector<float>> MatrixOne2Two(std::vector<float> matrixOne, int line, int column){
    //先定义
    std::vector<std::vector<float>> matrixTwo(line);
    for (int i=0;i<matrixTwo.size();i++){
        matrixTwo[i].resize(column);
    }
    int i=0, j=0;

    //将一维数组转化为二维
    for (int m=0;m<matrixOne.size();m++){
        i=m/column;
        j=m%column;
        matrixTwo[i][j] = matrixOne[m];
    }
    return matrixTwo;

}

//生成全零矩阵
//std::vector<std::vector<float>> MatrixZeroFloat(int line, int column){
//    //先定义
//    std::vector<std::vector<float>> matrixZero(line);
//    for (int i=0;i<matrixZero.size();i++){
//        matrixZero[i].resize(column);
//    }
//
//    for (int i=0;i<matrixZero.size();i++){
//        for (int j=0;j<matrixZero.size();j++){
//            matrixZero[i][j] = 0.0;
//        }
//    }
//    return matrixZero;
//}
//
//生成全零矩阵
//std::vector<std::vector<int>> MatrixZeroInt(int line, int column){
//    //先定义
//    std::vector<std::vector<int>> matrixZeroint(line);
//    for (int i=0;i<matrixZeroint.size();i++){
//        matrixZeroint[i].resize(column);
//    }
//
//    for (int i=0;i<matrixZeroint.size();i++){
//        for (int j=0;j<matrixZeroint.size();j++){
//            matrixZeroint[i][j] = 0;
//        }
//    }
//    return matrixZeroint;
//}


//对矩阵的某一行赋值
std::vector<std::vector<float>> MatrixReplaceline(std::vector<std::vector<float>> matrix, std::vector<float> oneLine, int line){
    std::vector<std::vector<float>> replacematrix = matrix;
    for(int j=0;j<matrix[line].size();j++){
        replacematrix[line][j] = oneLine[j];
    }
    return replacematrix;
}

std::vector<std::vector<int>> MatrixReplacelineInt(std::vector<std::vector<int>> matrix, std::vector<int> oneLine, int line){
    std::vector<std::vector<int>> replacematrixInt = matrix;
    for(int j=0;j<matrix[line].size();j++){
        replacematrixInt[line][j] = oneLine[j];
    }
    return replacematrixInt;
}


//对矩阵和列相加
std::vector<std::vector<float>> MatrixAddline(std::vector<std::vector<float>> matrix, std::vector<float> oneLine){
    std::vector<std::vector<float>> addmatrix = matrix;

    for(int i=0; i< matrix.size(); i++)
    {
        for(int j=0;j<matrix[i].size();j++)
        {
            addmatrix[i][j] = matrix[i][j] + oneLine[i];
        }
    }


    return addmatrix;
}

//两个vector相加
std::vector<float> vectorAddvector(std::vector<float> onevector, std::vector<float> twovector){
    std::vector<float> addvector = onevector;

    for(int i=0; i< onevector.size(); i++)
    {
        addvector[i] = onevector[i] + twovector[i];
    }

    return addvector;
}


//取矩阵每一列最大值输出
std::vector<float> MatrixMaxColomn(std::vector<std::vector<float>> matrix){
    std::vector<float> onecolumn;
    std::vector<float> oneMaxColomn(matrix[0].size());

    for(int i=0; i< matrix[0].size(); i++)
    {
        onecolumn = GetMatrixColumn(matrix, i);
        auto maxPosition = max_element(onecolumn.begin(), onecolumn.end());
        oneMaxColomn[i] = *maxPosition;
    }

    return oneMaxColomn;
}

//取矩阵每一列最大值index输出
std::vector<int> MatrixMaxColomnIndex(std::vector<std::vector<float>> matrix){
    std::vector<float> onecolumn;
    std::vector<int> oneMaxColomnIndex(matrix[0].size());

    for(int i=0; i< matrix[0].size(); i++)
    {
        onecolumn = GetMatrixColumn(matrix, i);
        auto maxPosition = max_element(onecolumn.begin(), onecolumn.end());
        oneMaxColomnIndex[i] = maxPosition - onecolumn.begin();
    }

    return oneMaxColomnIndex;
}






int main() {

    //step1
    //构造2个一维数组
    float ascore[40] = {-26.027508, -30.446663, -32.095524, -32.845524, -5.587373, -6.759389, -10.926412, -8.413100,
                        -21.166603, -23.149029, -25.346634, -21.894779, 2.402660, 11.540352, -7.339636, -6.628058,
                        44.774940, 41.914070, 44.076794, 47.784664, 53.988213, 50.826843, 54.131771, 54.337772,
                        44.029934, 40.224350, 43.935413, 45.182701, 34.802212, 31.385918, 34.385857, 33.761864,
                        25.966980, 22.973921, 24.499361, 25.053926, 8.182451, -4.396477, -5.321798, 8.880457};
    std::vector<float> score(ascore, ascore + 40);
    std::vector<std::vector<float>> scorematrix;
    scorematrix = MatrixOne2Two(score, 10, 4);

    float atransitions[16] = {0.528014, -5.869185, -22.835735, -21.817001, -13.961705, -27.572929, 2.904173, 2.449105,
                              -24.472170, -28.298948, 1.935582, 1.913870, -7.580759, -28.631573, -26.004593,
                              -25.073975};
    std::vector<float> transitions(atransitions, atransitions + 16);
    std::vector<std::vector<float>> transitionsatrix;
    transitionsatrix = MatrixOne2Two(transitions, 4, 4);


    std::vector<std::vector<float>> trellis(10, std::vector<float>(4,0.0));
//    trellis = MatrixZeroFloat(10,4);
    std::vector<std::vector<int>> backpointers(10, std::vector<int>(4,0));
//    backpointers = MatrixZeroInt(10,4);


    //step2
    std::vector<float> oneline;
    oneline = GetMatrixLine(scorematrix, 0);

    trellis = MatrixReplaceline(trellis, oneline, 0);

    std::vector<std::vector<float>> vmatrix;
    std::vector<float> maxcolumn;
    std::vector<float> b1;
    std::vector<int> b2;
    for (int t = 1; t < scorematrix.size(); t++) {
        oneline = GetMatrixLine(trellis, t-1);
        vmatrix = MatrixAddline(transitionsatrix, oneline);
        maxcolumn = MatrixMaxColomn(vmatrix);
        b1 = vectorAddvector(maxcolumn, GetMatrixLine(scorematrix, t));
        trellis = MatrixReplaceline(trellis, b1, t);
        b2 = MatrixMaxColomnIndex(vmatrix);
        backpointers = MatrixReplacelineInt(backpointers, b2, t);

    }

    //step3
    std::vector<int> viterbi;
    oneline = GetMatrixLine(trellis, 9);
    auto maxPosition = max_element(oneline.begin(), oneline.end());
    viterbi.push_back(maxPosition - oneline.begin());

    std::vector<int> bp;
    for (int i = 9; i > 0; i--) {
        bp = GetMatrixLineInt(backpointers, i);
        viterbi.push_back(bp[viterbi.back()]);
    }
    std::reverse(std::begin(viterbi), std::end(viterbi));


    //step4:输出结果-用来调试
    for(int t1=0; t1< backpointers.size(); t1++)//输出二维动态数组
    {
        for(int t2=0;t2<backpointers[t1].size();t2++)
        {
            cout<<backpointers[t1][t2]<<" ";
        }
        cout<<"backpointers" <<endl;
    }


    for(int t2=0;t2<viterbi.size();t2++)
    {
        cout<<viterbi[t2]<<" ";
    }
    cout<<"viterbi" <<endl;



    cout<<"结束" <<endl;

    return 0;

}
