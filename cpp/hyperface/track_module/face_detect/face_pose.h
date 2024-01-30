//
// Created by Tunm-Air13 on 2023/9/8.
//
#pragma once
#ifndef HYPERFACEREPO_FACEPOSE_H
#define HYPERFACEREPO_FACEPOSE_H

#include "../../data_type.h"
#include "middleware/any_net.h"

namespace inspire {

class HYPER_API FacePose : public AnyNet {
public:

    explicit FacePose();

    std::vector<float> operator()(const Matrix& bgr_affine);

};

}   // namespace hyper

#endif //HYPERFACEREPO_FACEPOSE_H
