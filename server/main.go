package main

import (
	"context"
	"fmt"
	"log"
	"net"

	pb "github.com/UCSC-CSE123/snowdrop/server/snowdrop"
	"google.golang.org/grpc"
)

type server struct {
	pb.UnimplementedEchoServer
}

func (s server) EchoMe(ctx context.Context, req *pb.EchoRequest) (*pb.EchoResponse, error) {
	return &pb.EchoResponse{
		Body: fmt.Sprintf("Hi User %d! You asked me to echo this: %q\n", req.GetIDNumber(), req.GetBody()),
	}, nil
}

func main() {
	lis, err := net.Listen("tcp", "0.0.0.0:8080")
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	pb.RegisterEchoServer(s, server{})
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
