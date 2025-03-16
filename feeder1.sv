module signer16bmod2 (
    input bit [15:0] a,
    input bit dog,
    output bit [15:0] mag,
    output bit feeder
);

  always_comb begin
    all1   = 1'b0;
    feeder = 1'b0;
    if (dog == 1'b0) begin
      mag = a;
    end else if (a[8] == 1'b0) mag = {a[15:9], 1'd1, 8'd0};
    else if (a[9] == 1'b0) mag = {a[15:10], 1'd1, 9'd0};
    else if (a[10] == 1'b0) mag = {a[15:11], 1'd1, 10'd0};
    else if (a[11] == 1'b0) mag = {a[15:12], 1'd1, 11'd0};
    else begin
      mag = a;
      feeder = 1'b1;

    end
  end

endmodule
