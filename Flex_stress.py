# sigma_top, sigma_bottom and tau_glue are solid
# sigma_depth should be solid but is untested rigerously.
# tau_cent could cause problems because it uses
# Bridge_geometry.thickness, which does not handle
# edge cases well (finding thickness at intersection)
# of beams. In most cases, tau_cent should be accurate

import Bridge_geometry

def sigma_depth(beam_list, M, dist_from_bottom):
    I = Bridge_geometry.I(beam_list)
    h = dist_from_bottom
    yb = Bridge_geometry.y_bar(beam_list)
    return M * abs(h - yb) / I

def sigma_top(beam_list, M):
    I = Bridge_geometry.I(beam_list)
    h = Bridge_geometry.y_top(beam_list)
    yb = Bridge_geometry.y_bar(beam_list)
    return M * (h - yb) / I

def sigma_bottom(beam_list, M):
    I = Bridge_geometry.I(beam_list)
    yb = Bridge_geometry.y_bar(beam_list)
    return M * yb / I

def tau_cent(beam_list, V):
    yb = Bridge_geometry.y_bar(beam_list)
    Q = Bridge_geometry.Q(beam_list, yb)
    I = Bridge_geometry.I(beam_list)
    b_c = Bridge_geometry.horizontal_thickness(beam_list, yb)
    return V * Q / (I * b_c)

def tau_glue(beam_list, V, depth_of_interest, glue_width):
    h = depth_of_interest
    Q = Bridge_geometry.Q(beam_list, h)
    I = Bridge_geometry.I(beam_list)
    return V * Q / (I * glue_width)
